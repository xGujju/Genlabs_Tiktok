"""Thai/Latin text normalization and similarity helpers.

Pure stdlib. No tokenizer required: Thai is written without word breaks,
so character-bigrams are a robust similarity proxy that also works for
mixed Thai/Latin text (tool names like ChatGPT, NotebookLM).
"""
from __future__ import annotations

import re
import unicodedata
from typing import Iterable

# Thai pai-yan-noi (ฯ), mai-yamok (ๆ) treated as punctuation.
_PUNCT = re.compile(r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~ฯๆ]+")
_WHITESPACE = re.compile(r"\s+")
_DIGITS = re.compile(r"[\d๐-๙]+")  # ASCII + Thai numerals


def normalize_text(s: str) -> str:
    """NFC + lowercase + strip punctuation/digits + collapse whitespace."""
    if not s:
        return ""
    s = unicodedata.normalize("NFC", s)
    s = s.lower()
    s = _PUNCT.sub(" ", s)
    s = _DIGITS.sub(" ", s)
    s = _WHITESPACE.sub(" ", s)
    return s.strip()


def char_bigrams(s: str) -> set[str]:
    """Character bigrams over a normalized string, skipping whitespace pairs."""
    if not s:
        return set()
    chars = [c for c in s if not c.isspace()]
    if len(chars) < 2:
        return set()
    return {chars[i] + chars[i + 1] for i in range(len(chars) - 1)}


def jaccard(a: Iterable[str], b: Iterable[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def text_similarity(a: str, b: str) -> float:
    """Char-bigram Jaccard similarity on normalized text. Range [0, 1]."""
    return jaccard(char_bigrams(normalize_text(a)), char_bigrams(normalize_text(b)))


# ---------- tool detection ----------
# Surface aliases are matched against normalized text. Order within a tool's
# alias list doesn't matter; cross-tool ordering does not either since we
# return *first occurrence* in the source string.

TOOL_ALIASES: dict[str, tuple[str, ...]] = {
    "chatgpt":        ("chatgpt", "chat gpt", "gpt-4", "gpt-5", "gpt-5.5", "custom gpt", "openai gpt"),
    "claude":         ("claude", "anthropic"),
    "claude_code":    ("claude code", "claude-code", "claudecode"),
    "claude_artifacts": ("claude artifact", "claude project"),
    "notebooklm":     ("notebooklm", "notebook lm", "notebook-lm"),
    "perplexity":     ("perplexity",),
    "canva":          ("canva",),
    "capcut":         ("capcut", "cap cut"),
    "gamma":          ("gamma app", " gamma "),
    "gemini":         ("gemini",),
    "midjourney":     ("midjourney",),
    "sora":           ("sora ",),
    "runway":         ("runway",),
    "cursor":         ("cursor ",),
    "windsurf":       ("windsurf",),
    "n8n":            ("n8n",),
    "zapier":         ("zapier",),
    "make":           ("make.com", "integromat"),
    "kling":          ("kling",),
    "flux":           ("flux ",),
    "mcp":            (" mcp", "model context protocol"),
    "line_oa":        ("line oa", "line@", "line official account"),
    "shopify":        ("shopify",),
    "lazada":         ("lazada",),
    "shopee":         ("shopee",),
    "grabfood":       ("grabfood", "grab food"),
    "lineman":        ("lineman", "line man"),
    "tiktok_shop":    ("tiktok shop", "tiktokshop"),
}


def _scan_tools(text: str) -> list[tuple[int, str]]:
    """Greedy left-to-right scan, longest-alias-wins at each position.

    Ensures "Claude Code" matches `claude_code` rather than `claude`.
    Returns list of (position, tool) in scan order.
    """
    pairs: list[tuple[str, str]] = [
        (alias, tool)
        for tool, aliases in TOOL_ALIASES.items()
        for alias in aliases
    ]
    pairs.sort(key=lambda p: -len(p[0]))  # longest aliases first

    out: list[tuple[int, str]] = []
    pos = 0
    n = len(text)
    while pos < n:
        for alias, tool in pairs:
            if text.startswith(alias, pos):
                out.append((pos, tool))
                pos += len(alias)
                break
        else:
            pos += 1
    return out


def detect_primary_tool(text: str) -> str | None:
    """First-occurring tool name in normalized text, or None."""
    if not text:
        return None
    hits = _scan_tools(normalize_text(text))
    return hits[0][1] if hits else None


def detect_all_tools(text: str) -> list[str]:
    """All tools mentioned, in order of first occurrence, deduplicated."""
    if not text:
        return []
    hits = _scan_tools(normalize_text(text))
    seen: set[str] = set()
    out: list[str] = []
    for _, t in hits:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out
