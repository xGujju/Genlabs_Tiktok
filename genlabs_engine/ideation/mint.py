"""Idea mint: compose signal wells → score against avatars + novelty → rank.

Output: candidates_queue.jsonl
  one row per (signal, avatar) candidate that passes minimum gates.

Downstream: production reads the queue and renders the top-N for the day.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from ..avatars import AvatarRegistry
from ..cooldown import CooldownDB
from ..signals import (
    VOICE_SIGNALS_PATH,
    WEB_SIGNALS_PATH,
    X_SIGNALS_PATH,
    YOUTUBE_SIGNALS_PATH,
    RawSignal,
    read_signals,
    utc_now_iso,
)
from .score import (
    detect_primary_tool_for_signal,
    score_action_density,
    score_avatar_fit,
    score_local_fit,
    score_pain_acuity,
    score_recency,
)

# Default scoring weights — sum to 1.0 over positive features.
# Tunable later by the learning layer via config/runtime/scoring_weights.yaml.
DEFAULT_WEIGHTS: dict[str, float] = {
    "avatar_fit":     0.30,
    "pain_acuity":    0.20,
    "action_density": 0.15,
    "local_fit":      0.10,
    "novelty":        0.20,
    "recency":        0.05,
}

DEFAULT_MIN_AVATAR_FIT = 0.30
DEFAULT_MIN_SCORE = 0.45
DEFAULT_TOP_PER_AVATAR = 8


@dataclass
class Candidate:
    candidate_id: str
    minted_at: str
    avatar_id: str
    signal_post_id: str
    signal_well: str
    signal_url: str
    signal_text_preview: str
    primary_tool: str | None
    search_theme: str
    final_score: float
    features: dict[str, float] = field(default_factory=dict)
    novelty: dict = field(default_factory=dict)
    blocked_reason: str | None = None

    def to_jsonl(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


def all_signal_paths() -> list[Path]:
    return [X_SIGNALS_PATH, WEB_SIGNALS_PATH, YOUTUBE_SIGNALS_PATH, VOICE_SIGNALS_PATH]


def load_all_signals(paths: list[Path] | None = None) -> list[RawSignal]:
    paths = paths or all_signal_paths()
    signals: list[RawSignal] = []
    for p in paths:
        signals.extend(read_signals(p))
    return signals


def mint_candidates(
    registry: AvatarRegistry,
    signals: list[RawSignal],
    cooldown: CooldownDB,
    *,
    weights: dict[str, float] | None = None,
    min_avatar_fit: float = DEFAULT_MIN_AVATAR_FIT,
    min_score: float = DEFAULT_MIN_SCORE,
    top_per_avatar: int = DEFAULT_TOP_PER_AVATAR,
    lookback_days_novelty: int = 30,
    require_novel: bool = True,
) -> list[Candidate]:
    """Score every (signal × avatar) pair, drop poor matches, return top-N per avatar."""
    w = {**DEFAULT_WEIGHTS, **(weights or {})}
    per_avatar: dict[str, list[Candidate]] = {a.id: [] for a in registry}
    minted_at = utc_now_iso()

    for signal in signals:
        primary_tool = detect_primary_tool_for_signal(signal)
        # If signal was discovered for a specific avatar, prefer-but-don't-restrict.
        for avatar in registry:
            fit = score_avatar_fit(signal, avatar)
            if fit < min_avatar_fit:
                continue

            novelty = cooldown.check_novelty(
                topic=signal.text[:200],
                hook=signal.text[:120],
                primary_tool=primary_tool,
                avatar_id=avatar.id,
                lookback_days=lookback_days_novelty,
            )

            features = {
                "avatar_fit":     fit,
                "pain_acuity":    score_pain_acuity(signal),
                "action_density": score_action_density(signal),
                "local_fit":      score_local_fit(signal, avatar),
                "novelty":        1.0 if novelty.is_novel else 0.0,
                "recency":        score_recency(signal),
            }
            final = sum(w[k] * features[k] for k in features)

            blocked = None
            if require_novel and not novelty.is_novel:
                blocked = f"novelty: {novelty.reason}"
            elif final < min_score:
                blocked = f"low score ({final:.2f} < {min_score})"

            cand = Candidate(
                candidate_id=f"{signal.well}:{signal.post_id}:{avatar.id}",
                minted_at=minted_at,
                avatar_id=avatar.id,
                signal_post_id=signal.post_id,
                signal_well=signal.well,
                signal_url=signal.post_url,
                signal_text_preview=signal.text[:240],
                primary_tool=primary_tool,
                search_theme=signal.search_theme,
                final_score=round(final, 4),
                features={k: round(v, 4) for k, v in features.items()},
                novelty=novelty.to_dict(),
                blocked_reason=blocked,
            )
            if blocked is None:
                per_avatar[avatar.id].append(cand)

    # Rank per avatar and take top N
    out: list[Candidate] = []
    for aid, lst in per_avatar.items():
        lst.sort(key=lambda c: c.final_score, reverse=True)
        out.extend(lst[:top_per_avatar])
    out.sort(key=lambda c: c.final_score, reverse=True)
    return out


def write_queue(candidates: list[Candidate], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for c in candidates:
            f.write(c.to_jsonl() + "\n")
