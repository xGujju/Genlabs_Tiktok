"""SQLite-backed novelty + variety enforcement registry.

The cooldown DB answers two questions for the production engine:

    1. "Have we recently covered this idea?"  → novelty check
    2. "How is today's output distributed across avatar/format/tool/hook?"
       → variety stats

DB location: ~/.hermes/genlabs_state/cooldown.sqlite (override with
GENLABS_COOLDOWN_DB env var). The DB is *not* in the operational repo —
it's machine-local state and would be noise in git history.
"""
from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterator

from ._thai import char_bigrams, jaccard, normalize_text
from .manifest import ParsedCarousel

def _default_state_dir() -> Path:
    """State dir resolution order:
    1. $GENLABS_STATE_DIR  (explicit override)
    2. $HERMES_HOME/genlabs_state  (if HERMES_HOME is set)
    3. /home/clawd/.hermes/genlabs_state  (production default)
    4. ~/.hermes/genlabs_state  (last-resort fallback)
    """
    env = os.environ.get("GENLABS_STATE_DIR")
    if env:
        return Path(env)
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home) / "genlabs_state"
    production = Path("/home/clawd/.hermes/genlabs_state")
    if production.parent.exists():
        return production
    return Path.home() / ".hermes" / "genlabs_state"


DEFAULT_DB_PATH = Path(
    os.environ.get("GENLABS_COOLDOWN_DB", str(_default_state_dir() / "cooldown.sqlite"))
)


SCHEMA = """
CREATE TABLE IF NOT EXISTS published_posts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_key      TEXT UNIQUE NOT NULL,
    source_type     TEXT NOT NULL,
    source_id       TEXT,
    source_url      TEXT,
    topic_normalized TEXT NOT NULL,
    topic_raw       TEXT,
    hook_thai       TEXT,
    primary_tool    TEXT,
    secondary_tools TEXT,
    avatar_id       TEXT,
    format          TEXT NOT NULL,
    hook_frame      TEXT,
    slide_count     INTEGER,
    published_at    TEXT NOT NULL,
    manifest_path   TEXT,
    performance_views           INTEGER,
    performance_followers_delta INTEGER,
    performance_qualified_dms   INTEGER,
    created_at      TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_pub_topic  ON published_posts(topic_normalized);
CREATE INDEX IF NOT EXISTS idx_pub_avatar ON published_posts(avatar_id);
CREATE INDEX IF NOT EXISTS idx_pub_tool   ON published_posts(primary_tool);
CREATE INDEX IF NOT EXISTS idx_pub_date   ON published_posts(published_at);

CREATE TABLE IF NOT EXISTS topic_fingerprints (
    post_id        INTEGER PRIMARY KEY,
    bigrams        TEXT NOT NULL,           -- full carousel-text bigrams (space-separated)
    hook_bigrams   TEXT NOT NULL DEFAULT '',-- hook-slide-only bigrams
    full_text      TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES published_posts(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS cooldown_overrides (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    key_type     TEXT NOT NULL,
    key_value    TEXT NOT NULL,
    cooldown_days INTEGER NOT NULL,
    reason       TEXT,
    created_at   TEXT DEFAULT (datetime('now')),
    expires_at   TEXT
);
CREATE INDEX IF NOT EXISTS idx_override_key ON cooldown_overrides(key_type, key_value);

CREATE TABLE IF NOT EXISTS daily_variety_stats (
    date         TEXT NOT NULL,
    bucket       TEXT NOT NULL,
    bucket_value TEXT NOT NULL,
    count        INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (date, bucket, bucket_value)
);
"""


@dataclass
class NoveltyResult:
    is_novel: bool
    similarity: float
    hook_jaccard: float
    containment: float
    nearest_post_id: int | None
    nearest_source_key: str | None
    nearest_topic: str | None
    nearest_hook: str | None
    nearest_published_at: str | None
    reason: str
    days_to_nearest: int | None = None

    def to_dict(self) -> dict:
        return {
            "is_novel": self.is_novel,
            "similarity": round(self.similarity, 4),
            "hook_jaccard": round(self.hook_jaccard, 4),
            "containment": round(self.containment, 4),
            "nearest_post_id": self.nearest_post_id,
            "nearest_source_key": self.nearest_source_key,
            "nearest_topic": self.nearest_topic,
            "nearest_hook": self.nearest_hook,
            "nearest_published_at": self.nearest_published_at,
            "days_to_nearest": self.days_to_nearest,
            "reason": self.reason,
        }


@dataclass
class PublishedPost:
    source_key: str
    source_type: str
    topic_raw: str
    hook_thai: str
    format: str
    published_at: datetime
    full_text: str = ""
    source_id: str | None = None
    source_url: str | None = None
    primary_tool: str | None = None
    secondary_tools: list[str] = field(default_factory=list)
    avatar_id: str | None = None
    hook_frame: str | None = "tutorial_numbered"
    slide_count: int = 0
    manifest_path: str | None = None


def _utc_iso(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()


class CooldownDB:
    """Open() opens (and creates) the DB. Always close() when done, or use as ctx mgr."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = Path(path or DEFAULT_DB_PATH)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self.path))
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(SCHEMA)

    @classmethod
    def open(cls, path: Path | None = None) -> "CooldownDB":
        return cls(path)

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> "CooldownDB":
        return self

    def __exit__(self, *_exc) -> None:
        self.close()

    @contextmanager
    def _tx(self) -> Iterator[sqlite3.Connection]:
        try:
            yield self._conn
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise

    # ---------- ingest ----------

    def ingest_published(self, post: PublishedPost) -> int | None:
        """Insert post. Returns new row id, or None if source_key already existed."""
        topic_norm = normalize_text(f"{post.topic_raw} {post.hook_thai} {post.primary_tool or ''}")
        full = post.full_text or post.hook_thai
        bigrams = " ".join(sorted(char_bigrams(normalize_text(full))))
        hook_bigrams = " ".join(
            sorted(char_bigrams(normalize_text(f"{post.hook_thai} {post.primary_tool or ''}")))
        )
        with self._tx() as conn:
            cur = conn.execute(
                """INSERT OR IGNORE INTO published_posts
                   (source_key, source_type, source_id, source_url, topic_normalized,
                    topic_raw, hook_thai, primary_tool, secondary_tools, avatar_id,
                    format, hook_frame, slide_count, published_at, manifest_path)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (
                    post.source_key, post.source_type, post.source_id, post.source_url,
                    topic_norm, post.topic_raw, post.hook_thai, post.primary_tool,
                    ",".join(post.secondary_tools) if post.secondary_tools else None,
                    post.avatar_id, post.format, post.hook_frame, post.slide_count,
                    _utc_iso(post.published_at), post.manifest_path,
                ),
            )
            if cur.rowcount == 0:
                return None
            post_id = cur.lastrowid
            conn.execute(
                """INSERT OR REPLACE INTO topic_fingerprints
                   (post_id, bigrams, hook_bigrams, full_text)
                   VALUES (?,?,?,?)""",
                (post_id, bigrams, hook_bigrams, full),
            )
            day = post.published_at.astimezone(timezone.utc).date().isoformat()
            for bucket, value in (
                ("avatar", post.avatar_id),
                ("format", post.format),
                ("primary_tool", post.primary_tool),
                ("hook_frame", post.hook_frame),
                ("source_type", post.source_type),
            ):
                if value:
                    conn.execute(
                        """INSERT INTO daily_variety_stats (date, bucket, bucket_value, count)
                           VALUES (?, ?, ?, 1)
                           ON CONFLICT(date, bucket, bucket_value)
                           DO UPDATE SET count = count + 1""",
                        (day, bucket, value),
                    )
            return post_id

    def ingest_parsed_carousel(self, parsed: ParsedCarousel) -> int | None:
        return self.ingest_published(
            PublishedPost(
                source_key=parsed.folder_name,
                source_type=parsed.source_type,
                source_id=parsed.source_id,
                source_url=parsed.source_url,
                topic_raw=parsed.topic_raw,
                hook_thai=parsed.hook_thai,
                format=parsed.format,
                hook_frame=parsed.hook_frame,
                published_at=parsed.published_at,
                full_text=parsed.full_text,
                primary_tool=parsed.primary_tool,
                secondary_tools=parsed.secondary_tools,
                avatar_id=parsed.avatar_id,
                slide_count=parsed.slide_count,
                manifest_path=parsed.manifest_path,
            )
        )

    # ---------- novelty ----------

    def check_novelty(
        self,
        topic: str,
        hook: str | None = None,
        primary_tool: str | None = None,
        avatar_id: str | None = None,
        lookback_days: int = 30,
        hook_block_threshold: float = 0.35,
        containment_block_threshold: float = 0.80,
    ) -> NoveltyResult:
        """Return novelty verdict against posts in [now-lookback_days, now].

        Two independent block triggers (an idea is blocked if *either* fires):

          - hook_jaccard >= hook_block_threshold (default 0.35)
              The candidate hook is too similar to a prior hook. Hook is the
              strongest signal — it's what TikTok viewers see first, and even
              partial overlap reads as a duplicate.

          - containment >= containment_block_threshold (default 0.80)
              The candidate's bigrams are mostly contained in a prior carousel's
              full text. Catches rephrasings where the hook differs but the
              substance is the same.

        Calibrated against the 207-row back-fill of existing carousels. The
        same-tool / same-avatar adjacency adds +0.05 to each signal because
        repetition feels worse inside the same lane.

        Returns `similarity = max(hook_jaccard, containment)` for diagnostics
        but blocking is driven by the per-signal thresholds.
        """
        hook_text = hook or topic
        candidate_full = normalize_text(f"{topic} {hook_text} {primary_tool or ''}")
        candidate_hook = normalize_text(f"{hook_text} {primary_tool or ''}")
        cand_full_bg = char_bigrams(candidate_full)
        cand_hook_bg = char_bigrams(candidate_hook)
        if not cand_full_bg:
            return NoveltyResult(
                False, 0.0, 0.0, 0.0, None, None, None, None, None, "empty candidate text"
            )

        cutoff = (datetime.now(timezone.utc) - timedelta(days=lookback_days)).isoformat()
        cur = self._conn.execute(
            """SELECT p.id, p.source_key, p.topic_raw, p.hook_thai, p.published_at,
                      p.primary_tool, p.avatar_id, f.bigrams, f.hook_bigrams
                 FROM published_posts p
                 JOIN topic_fingerprints f ON f.post_id = p.id
                WHERE p.published_at >= ?""",
            (cutoff,),
        )
        best_signal = -1.0  # max(hook_j_adj, contain_adj) used to pick nearest
        best_hook_j = 0.0
        best_contain = 0.0
        best_row: sqlite3.Row | None = None
        best_hook_j_adj = 0.0
        best_contain_adj = 0.0
        for row in cur:
            other_full = set(row["bigrams"].split()) if row["bigrams"] else set()
            other_hook = set(row["hook_bigrams"].split()) if row["hook_bigrams"] else set()
            hook_j = jaccard(cand_hook_bg, other_hook) if other_hook else 0.0
            contain = (
                len(cand_full_bg & other_full) / len(cand_full_bg) if other_full else 0.0
            )
            hook_j_adj, contain_adj = hook_j, contain
            if primary_tool and row["primary_tool"] == primary_tool:
                hook_j_adj = min(1.0, hook_j_adj + 0.05)
                contain_adj = min(1.0, contain_adj + 0.05)
            if avatar_id and row["avatar_id"] == avatar_id:
                hook_j_adj = min(1.0, hook_j_adj + 0.05)
                contain_adj = min(1.0, contain_adj + 0.05)
            signal = max(hook_j_adj, contain_adj)
            if signal > best_signal:
                best_signal = signal
                best_hook_j = hook_j
                best_contain = contain
                best_hook_j_adj = hook_j_adj
                best_contain_adj = contain_adj
                best_row = row

        if best_row is None:
            return NoveltyResult(
                True, 0.0, 0.0, 0.0, None, None, None, None, None,
                f"no posts in last {lookback_days}d",
            )

        pub_dt = datetime.fromisoformat(best_row["published_at"])
        days_ago = max(0, (datetime.now(timezone.utc) - pub_dt).days)
        hook_block = best_hook_j_adj >= hook_block_threshold
        contain_block = best_contain_adj >= containment_block_threshold
        is_novel = not (hook_block or contain_block)
        trigger = (
            "hook" if hook_block and not contain_block
            else "containment" if contain_block and not hook_block
            else "hook+containment" if hook_block else "—"
        )
        verdict = "novel" if is_novel else f"too similar (trigger={trigger})"
        reason = (
            f"{verdict} vs {best_row['source_key']} "
            f"(hook_j={best_hook_j:.2f} contain={best_contain:.2f}, {days_ago}d ago)"
        )
        return NoveltyResult(
            is_novel=is_novel,
            similarity=max(best_hook_j, best_contain),
            hook_jaccard=best_hook_j,
            containment=best_contain,
            nearest_post_id=best_row["id"],
            nearest_source_key=best_row["source_key"],
            nearest_topic=best_row["topic_raw"],
            nearest_hook=best_row["hook_thai"],
            nearest_published_at=best_row["published_at"],
            reason=reason,
            days_to_nearest=days_ago,
        )

    # ---------- variety / stats ----------

    def daily_counts(self, date: str | None = None) -> dict[str, dict[str, int]]:
        """{bucket: {value: count}} for given UTC date (default today)."""
        date = date or datetime.now(timezone.utc).date().isoformat()
        cur = self._conn.execute(
            "SELECT bucket, bucket_value, count FROM daily_variety_stats WHERE date = ?",
            (date,),
        )
        out: dict[str, dict[str, int]] = {}
        for row in cur:
            out.setdefault(row["bucket"], {})[row["bucket_value"]] = row["count"]
        return out

    def total_posts(self) -> int:
        return int(self._conn.execute("SELECT COUNT(*) FROM published_posts").fetchone()[0])

    def posts_by_source_type(self) -> dict[str, int]:
        cur = self._conn.execute(
            "SELECT source_type, COUNT(*) FROM published_posts GROUP BY source_type ORDER BY 2 DESC"
        )
        return {row[0]: row[1] for row in cur}

    def posts_by_primary_tool(self) -> dict[str, int]:
        cur = self._conn.execute(
            """SELECT COALESCE(primary_tool, '<none>'), COUNT(*)
                 FROM published_posts GROUP BY primary_tool ORDER BY 2 DESC"""
        )
        return {row[0]: row[1] for row in cur}

    def top_repeated_hooks(self, limit: int = 15) -> list[tuple[str, int]]:
        cur = self._conn.execute(
            """SELECT hook_thai, COUNT(*) c FROM published_posts
                WHERE hook_thai IS NOT NULL AND hook_thai != ''
                GROUP BY hook_thai HAVING c > 1 ORDER BY c DESC LIMIT ?""",
            (limit,),
        )
        return [(row[0], row[1]) for row in cur]

    def posts_in_window(self, days: int = 7) -> int:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
        return int(
            self._conn.execute(
                "SELECT COUNT(*) FROM published_posts WHERE published_at >= ?", (cutoff,)
            ).fetchone()[0]
        )
