"""Canonical signal format + JSONL well writer/reader.

Every discovery well (x_signals, web_signals, youtube_signals, voice_signals)
serializes to the same RawSignal shape so ideation can compose them uniformly.

JSONL is the storage format: one signal per line, append-only, deduped on
post_id. This is the simplest durable shape that survives the engine running
across multiple processes / cron jobs without locking ceremony.
"""
from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator


def _state_dir() -> Path:
    env = os.environ.get("GENLABS_STATE_DIR")
    if env:
        return Path(env)
    production = Path("/home/clawd/.hermes/genlabs_state")
    return production if production.parent.exists() else Path.home() / ".hermes" / "genlabs_state"


STATE_DIR = _state_dir()
X_SIGNALS_PATH = STATE_DIR / "x_signals.jsonl"
WEB_SIGNALS_PATH = STATE_DIR / "web_signals.jsonl"
YOUTUBE_SIGNALS_PATH = STATE_DIR / "youtube_signals.jsonl"
VOICE_SIGNALS_PATH = STATE_DIR / "voice_signals.jsonl"


@dataclass
class RawSignal:
    well: str                       # "x" | "web" | "youtube" | "voice"
    discovered_at: str              # ISO UTC
    post_id: str                    # source-stable identifier
    post_url: str
    text: str
    author_handle: str = ""
    author_name: str = ""
    author_followers: int = 0
    like_count: int = 0
    repost_count: int = 0
    reply_count: int = 0
    quote_count: int = 0
    bookmark_count: int = 0
    created_at: str = ""            # original post creation time (ISO if known)
    language: str = ""              # "en" | "th" | "" if unknown
    avatar_id: str = ""             # avatar this signal was sought for
    search_theme: str = ""          # the avatar.x_search_themes entry that surfaced it
    raw_payload: dict[str, Any] = field(default_factory=dict)

    def to_jsonl(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    @classmethod
    def from_jsonl(cls, line: str) -> "RawSignal":
        d = json.loads(line)
        return cls(**d)


class SignalsWriter:
    """Append-only JSONL writer with in-process dedup by (well, post_id)."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._seen: set[tuple[str, str]] = set()
        if self.path.exists():
            for sig in read_signals(self.path):
                self._seen.add((sig.well, sig.post_id))

    def append(self, signal: RawSignal) -> bool:
        """Append signal. Returns True if written, False if duplicate."""
        key = (signal.well, signal.post_id)
        if key in self._seen:
            return False
        with self.path.open("a", encoding="utf-8") as f:
            f.write(signal.to_jsonl() + "\n")
        self._seen.add(key)
        return True

    def append_many(self, signals: list[RawSignal]) -> tuple[int, int]:
        """Append a batch. Returns (written, skipped)."""
        written = 0
        skipped = 0
        for sig in signals:
            if self.append(sig):
                written += 1
            else:
                skipped += 1
        return written, skipped


def read_signals(path: Path) -> Iterator[RawSignal]:
    """Yield RawSignals from a JSONL file, skipping malformed lines silently."""
    if not path.exists():
        return
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield RawSignal.from_jsonl(line)
            except (json.JSONDecodeError, TypeError):
                continue


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
