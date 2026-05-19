#!/usr/bin/env python3
"""Idea mint: compose signal wells × avatars × novelty → ranked candidates."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml  # noqa: E402

from genlabs_engine.avatars import AvatarRegistry  # noqa: E402
from genlabs_engine.cooldown import CooldownDB  # noqa: E402
from genlabs_engine.ideation.mint import (  # noqa: E402
    DEFAULT_MIN_AVATAR_FIT,
    DEFAULT_MIN_SCORE,
    DEFAULT_TOP_PER_AVATAR,
    DEFAULT_WEIGHTS,
    load_all_signals,
    mint_candidates,
    write_queue,
)
from genlabs_engine.signals import (  # noqa: E402
    VOICE_SIGNALS_PATH,
    WEB_SIGNALS_PATH,
    X_SIGNALS_PATH,
    YOUTUBE_SIGNALS_PATH,
)

DEFAULT_QUEUE_PATH = Path(
    os.environ.get(
        "GENLABS_CANDIDATES_QUEUE",
        "/home/clawd/.hermes/genlabs_state/candidates_queue.jsonl",
    )
)
WEIGHTS_PATH = (
    Path(__file__).resolve().parent.parent / "config" / "runtime" / "scoring_weights.yaml"
)


def main() -> int:
    p = argparse.ArgumentParser(description="GenLabs idea-mint")
    p.add_argument("--wells", nargs="*",
                   choices=["x", "web", "youtube", "voice"],
                   default=["x", "web", "youtube", "voice"])
    p.add_argument("--top-per-avatar", type=int, default=DEFAULT_TOP_PER_AVATAR)
    p.add_argument("--min-avatar-fit", type=float, default=DEFAULT_MIN_AVATAR_FIT)
    p.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE)
    p.add_argument("--lookback-days", type=int, default=30)
    p.add_argument("--allow-non-novel", action="store_true",
                   help="Don't filter out candidates blocked by cooldown")
    p.add_argument("--output", type=Path, default=DEFAULT_QUEUE_PATH)
    p.add_argument("--weights-file", type=Path, default=WEIGHTS_PATH)
    p.add_argument("--summary", action="store_true",
                   help="Print human summary to stderr after writing the queue")
    args = p.parse_args()

    well_paths = {
        "x": X_SIGNALS_PATH, "web": WEB_SIGNALS_PATH,
        "youtube": YOUTUBE_SIGNALS_PATH, "voice": VOICE_SIGNALS_PATH,
    }
    paths = [well_paths[w] for w in args.wells]

    registry = AvatarRegistry.load()

    weights = dict(DEFAULT_WEIGHTS)
    min_avatar_fit = args.min_avatar_fit
    min_score = args.min_score
    require_novel = not args.allow_non_novel
    if args.weights_file.exists():
        cfg = yaml.safe_load(args.weights_file.read_text(encoding="utf-8")) or {}
        weights.update(cfg.get("weights", {}) or {})
        gates = cfg.get("gates", {}) or {}
        min_avatar_fit = float(gates.get("min_avatar_fit", min_avatar_fit))
        min_score = float(gates.get("min_score", min_score))
        if "require_novel" in gates and not args.allow_non_novel:
            require_novel = bool(gates["require_novel"])

    signals = load_all_signals(paths)
    if not signals:
        print(
            "WARNING: no signals found. Run x-discover / voice-listen first.",
            file=sys.stderr,
        )

    with CooldownDB.open() as db:
        candidates = mint_candidates(
            registry=registry,
            signals=signals,
            cooldown=db,
            weights=weights,
            min_avatar_fit=min_avatar_fit,
            min_score=min_score,
            top_per_avatar=args.top_per_avatar,
            lookback_days_novelty=args.lookback_days,
            require_novel=require_novel,
        )

    write_queue(candidates, args.output)

    per_avatar: dict[str, int] = {}
    for c in candidates:
        per_avatar[c.avatar_id] = per_avatar.get(c.avatar_id, 0) + 1

    summary = {
        "wells_read": args.wells,
        "signals_in": len(signals),
        "candidates_out": len(candidates),
        "per_avatar": per_avatar,
        "output": str(args.output),
    }
    if args.summary:
        print(json.dumps(summary, ensure_ascii=False, indent=2), file=sys.stderr)
    else:
        print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
