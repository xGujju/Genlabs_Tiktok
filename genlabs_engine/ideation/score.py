"""Candidate signal scoring features.

Each scorer returns a value in [0, 1] (or [-1, 0] for penalty signals).
Composition into a final candidate score is done in mint.py so the
weights can be tuned without touching this module.
"""
from __future__ import annotations

import math
import re
from datetime import datetime, timezone

from .._thai import (
    char_bigrams,
    detect_all_tools,
    detect_primary_tool,
    jaccard,
    normalize_text,
)
from ..avatars import Avatar
from ..signals import RawSignal


# Pain / urgency vocabulary — English + Thai.
PAIN_TERMS_EN = (
    "broken", "frustrated", "waste", "wasted", "lose", "losing", "lost", "missed",
    "miss", "struggle", "struggling", "can't", "cant", "stuck", "drowning", "behind",
    "manual", "hours", "tedious", "boring", "repetitive", "tired of", "exhausted",
    "annoying", "headache", "nightmare", "every day", "every week", "no time",
)
PAIN_TERMS_TH = (
    "ทำไงดี", "วุ่น", "พลาด", "เสีย", "ลำบาก", "ไม่ทัน", "ทับ",
    "ใช้เวลา", "หลายชั่วโมง", "เซ็ง", "เหนื่อย", "ปวดหัว", "ลืม",
    "เก็บไม่ทัน", "ตามไม่ทัน", "เครียด",
)

# Action / actionability vocabulary.
ACTION_TERMS_EN = (
    "try this", "copy this", "use this", "steal this", "do this", "follow this",
    "step 1", "step 2", "step 3", "first", "then", "finally", "checklist",
    "template", "framework", "playbook", "tutorial", "guide", "walkthrough",
    "how to", "in 5 minutes", "in 10 minutes", "5 steps", "3 steps",
    "free", "open source", "github", "repo", "prompt",
)
ACTION_TERMS_TH = (
    "ลองเลย", "ทำตาม", "ขั้นตอน", "วิธี", "สูตร", "template", "checklist",
    "ใน 5 นาที", "ฟรี",
)

# Thai-relevant local tools / platforms.
LOCAL_TH_TOOLS = (
    "line oa", "line@", "k-plus", "kplus", "ก พลัส", "scb easy", "true money",
    "shopee", "lazada", "tiktok shop", "grabfood", "grab food", "lineman", "line man",
    "foodpanda", "robinhood", "wongnai", "ddproperty", "hipflat",
    "flowaccount", "express", "peak account",
    "ภาษี", "สรรพากร", "ภงด", "ภพ",
)

# Numbered-tip patterns (English + Thai).
_NUMBERED_RE = re.compile(r"\b(\d+)\s*(?:steps|tips|ways|วิธี|ขั้น|ข้อ)\b", re.I)
_BULLET_RE = re.compile(r"(?:^|\n)\s*(?:[-•▪]|\d+\.)\s+", re.M)


def _term_hits(text_lower: str, terms: tuple[str, ...]) -> int:
    return sum(1 for t in terms if t in text_lower)


def score_pain_acuity(signal: RawSignal) -> float:
    """How acute does this signal sound? 0=flat, 1=urgent pain."""
    if not signal.text:
        return 0.0
    n = signal.text.lower()
    en_hits = _term_hits(n, PAIN_TERMS_EN)
    th_hits = _term_hits(normalize_text(signal.text), PAIN_TERMS_TH)
    total = en_hits + th_hits
    # Diminishing returns past 3 hits
    return min(1.0, total / 3.0)


def score_action_density(signal: RawSignal) -> float:
    """How actionable is this signal? Numbered tips + how-to verbs + links."""
    if not signal.text:
        return 0.0
    n = signal.text.lower()
    score = 0.0
    if _NUMBERED_RE.search(signal.text):
        score += 0.4
    bullet_count = len(_BULLET_RE.findall(signal.text))
    if bullet_count >= 3:
        score += 0.3
    elif bullet_count >= 1:
        score += 0.15
    en_hits = _term_hits(n, ACTION_TERMS_EN)
    th_hits = _term_hits(normalize_text(signal.text), ACTION_TERMS_TH)
    score += min(0.3, (en_hits + th_hits) * 0.05)
    if "http" in n or "github.com" in n:
        score += 0.1
    return min(1.0, score)


def score_local_fit(signal: RawSignal, avatar: Avatar) -> float:
    """Does this signal reference Thai-relevant tools or contexts?

    Most X signals are English-language global AI Twitter — they rarely
    mention Thai-specific tools. So local fit is naturally low. A signal
    that *does* mention LINE OA, Lazada, etc. is a strong positive.
    """
    if not signal.text:
        return 0.0
    n = signal.text.lower()
    hits = _term_hits(n, LOCAL_TH_TOOLS)
    if signal.language == "th":
        hits += 1
    return min(1.0, hits * 0.4)


def score_avatar_fit(signal: RawSignal, avatar: Avatar) -> float:
    """Multi-feature avatar-fit score in [0, 1].

    Composition:
      0.40  theme_match     — bigram sim of signal vs concat(x_search_themes)
      0.25  tool_match      — does signal mention a tool the avatar uses?
      0.20  pain_match_en   — substring hits in avatar.daily_pains[*].pain_en
      0.10  industry_match  — substring hit on industry/subindustry
      0.05  vocab_match     — substring hits in avatar.vocabulary.key_nouns
     -0.30  distrust_penalty — mentions a tool in avatar.tools_distrusted
     -0.20  avoid_penalty   — contains a phrase in avatar.avoid_phrases

    Clipped to [0, 1].
    """
    if not signal.text:
        return 0.0
    text_norm = normalize_text(signal.text)
    text_low = signal.text.lower()

    # theme_match
    themes = " ".join(avatar.x_search_themes)
    theme_match = jaccard(char_bigrams(text_norm), char_bigrams(normalize_text(themes))) if themes else 0.0

    # tool_match
    signal_tools = set(detect_all_tools(signal.text))
    avatar_tools = {t.strip().lower() for t in (avatar.raw.get("tools_used") or [])}
    tool_match = 0.0
    for t in signal_tools:
        token = t.replace("_", " ")
        if any(token in at or at in token for at in avatar_tools):
            tool_match = 1.0
            break

    # pain_match — concat pain_en phrases and look for partial overlaps
    pain_en_terms: list[str] = []
    for p in avatar.daily_pains + avatar.weekly_pains:
        pe = (p.get("pain_en") or "").lower()
        if pe:
            # crude: each pain becomes a multi-keyword check
            for w in re.findall(r"[a-z]{4,}", pe):
                pain_en_terms.append(w)
    pain_hits = sum(1 for w in set(pain_en_terms) if w in text_low)
    pain_match = min(1.0, pain_hits / 4.0)

    # industry_match
    industry_match = 0.0
    for kw in (avatar.industry, avatar.subindustry):
        for token in re.findall(r"[a-z]{3,}", (kw or "").lower()):
            if token in text_low:
                industry_match = 1.0
                break

    # vocab_match (Thai key nouns)
    key_nouns = [str(x).lower() for x in (avatar.raw.get("vocabulary", {}).get("key_nouns", []) or [])]
    vocab_hits = sum(1 for kn in key_nouns if kn and kn in signal.text.lower())
    vocab_match = min(1.0, vocab_hits / 3.0)

    # distrust_penalty
    distrust_terms = [str(t).lower() for t in (avatar.raw.get("tools_distrusted") or [])]
    distrust_penalty = 0.0
    for dt in distrust_terms:
        if dt and dt in text_low:
            distrust_penalty = 1.0
            break

    # avoid_penalty
    avoid_penalty = 0.0
    for ap in avatar.avoid_phrases:
        if ap and ap.lower() in text_low:
            avoid_penalty = 1.0
            break

    raw = (
        0.40 * theme_match
        + 0.25 * tool_match
        + 0.20 * pain_match
        + 0.10 * industry_match
        + 0.05 * vocab_match
        - 0.30 * distrust_penalty
        - 0.20 * avoid_penalty
    )
    return max(0.0, min(1.0, raw))


def score_recency(signal: RawSignal, half_life_hours: float = 36.0) -> float:
    """Exponential decay; 1.0 at signal.created_at == now."""
    if not signal.created_at:
        return 0.5  # unknown → middling
    try:
        # Accept both '2026-05-18T...' and X's '...+0000' forms.
        s = signal.created_at.replace("Z", "+00:00")
        dt = datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return 0.5
    hours = max(0.0, (datetime.now(timezone.utc) - dt).total_seconds() / 3600.0)
    return math.exp(-hours * math.log(2) / half_life_hours)


def detect_primary_tool_for_signal(signal: RawSignal) -> str | None:
    return detect_primary_tool(signal.text)
