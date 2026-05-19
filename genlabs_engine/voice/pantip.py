"""Pantip topic scraper (public read).

Pantip is the dominant Thai web forum for SME questions: /forum/business,
/forum/sinthorn (beauty/fashion), /forum/food, /forum/home (contractors),
/forum/condo (real estate). The HTML pages render through JS but each
forum has a public JSON endpoint that returns topic metadata.

This module uses urllib (stdlib only — no external deps) with a polite
default rate limit of ~1 req/sec. If Pantip ever changes their endpoint
shape, the parsing will degrade gracefully (no signals captured) rather
than throwing.

NOTE: respect Pantip's robots.txt and ToS. Public read of forum lists is
fine; do not scrape user profiles or login-gated content.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Iterable

from ..signals import RawSignal, utc_now_iso

PANTIP_FORUMS_OF_INTEREST = (
    "business",        # SME / business / startup
    "sinthorn",        # beauty / fashion / lifestyle
    "food",            # F&B / restaurants
    "home",            # home / contractor / DIY
    "condo",           # real estate
    "supachalasai",    # tech / IT / coding
)

USER_AGENT = "GenLabsThaiSMEVoiceListener/1.0 (+respect-robots.txt)"


@dataclass
class PantipTopic:
    topic_id: str
    title: str
    excerpt: str
    forum: str
    url: str
    posted_at: str
    likes: int = 0
    comments: int = 0


def fetch_forum_topics(
    forum: str,
    *,
    limit: int = 25,
    timeout: float = 15.0,
) -> list[PantipTopic]:
    """Fetch recent topics from a Pantip forum via the public list endpoint.

    Returns a (possibly empty) list. Never raises on parsing errors — returns
    [] so the caller can keep going on other forums.
    """
    url = (
        f"https://pantip.com/api/forum-service/forum/topics"
        f"?room={urllib.parse.quote(forum)}&limit={int(limit)}&type=topic"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8", errors="replace"))
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError, ConnectionError):
        return []

    topics_raw = (
        payload.get("data", {}).get("topics")
        or payload.get("topics")
        or payload.get("data", [])
    )
    if not isinstance(topics_raw, list):
        return []

    out: list[PantipTopic] = []
    for t in topics_raw:
        if not isinstance(t, dict):
            continue
        tid = str(t.get("topic_id") or t.get("id") or "")
        if not tid:
            continue
        title = str(t.get("title") or t.get("topic_title") or "").strip()
        excerpt = str(t.get("desc") or t.get("excerpt") or t.get("body") or "").strip()
        out.append(
            PantipTopic(
                topic_id=tid,
                title=title,
                excerpt=excerpt,
                forum=forum,
                url=f"https://pantip.com/topic/{tid}",
                posted_at=str(t.get("post_time") or t.get("posted_at") or ""),
                likes=int(t.get("like_count") or t.get("votes") or 0),
                comments=int(t.get("comments_count") or t.get("comments") or 0),
            )
        )
    return out


def topic_to_signal(
    topic: PantipTopic,
    *,
    avatar_id: str = "",
    search_theme: str = "",
) -> RawSignal:
    text = topic.title
    if topic.excerpt:
        text = f"{topic.title}\n\n{topic.excerpt}"
    return RawSignal(
        well="voice",
        discovered_at=utc_now_iso(),
        post_id=f"pantip:{topic.topic_id}",
        post_url=topic.url,
        text=text,
        author_handle=f"pantip_{topic.forum}",
        author_name="",
        author_followers=0,
        like_count=topic.likes,
        repost_count=0,
        reply_count=topic.comments,
        created_at=topic.posted_at,
        language="th",
        avatar_id=avatar_id,
        search_theme=search_theme,
        raw_payload={"forum": topic.forum, "source": "pantip.com"},
    )


def harvest(
    forums: Iterable[str] = PANTIP_FORUMS_OF_INTEREST,
    *,
    per_forum: int = 25,
    delay_sec: float = 1.0,
    forum_to_avatar: dict[str, str] | None = None,
) -> list[RawSignal]:
    """Polite multi-forum harvest. Returns canonical RawSignals."""
    forum_to_avatar = forum_to_avatar or {}
    out: list[RawSignal] = []
    forums = list(forums)
    for i, forum in enumerate(forums):
        topics = fetch_forum_topics(forum, limit=per_forum)
        for t in topics:
            out.append(topic_to_signal(t, avatar_id=forum_to_avatar.get(forum, "")))
        if i < len(forums) - 1 and delay_sec > 0:
            time.sleep(delay_sec)
    return out
