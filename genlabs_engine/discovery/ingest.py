"""Normalize search results from various tools into canonical RawSignals.

Accepts JSON shapes from:
  - Hermes x_search results
  - Apify legacy actor results (so we can replay old data if needed)
  - generic web_search / browser hits
  - Pantip topic results

Outputs canonical RawSignals via signals.SignalsWriter.
"""
from __future__ import annotations

from typing import Any

from ..signals import RawSignal, utc_now_iso


def normalize_x_result(
    raw: dict[str, Any],
    avatar_id: str,
    search_theme: str,
) -> RawSignal | None:
    """Normalize one X (Twitter) post dict from Hermes x_search output.

    Hermes x_search returns posts roughly shaped like:
        {
          "id": "1234...", "text": "...", "url": "...",
          "author": {"username": "...", "name": "...", "followers": ...},
          "public_metrics": {"like_count": ..., "retweet_count": ..., ...},
          "created_at": "2026-05-...",
          "lang": "en"
        }
    Apify shape is similar but with slightly different keys; we tolerate
    both via .get() and a few aliases.
    """
    post_id = str(raw.get("id") or raw.get("post_id") or raw.get("tweet_id") or "")
    if not post_id:
        return None
    text = str(raw.get("text") or raw.get("full_text") or raw.get("content") or "").strip()
    if not text:
        return None
    url = str(raw.get("url") or raw.get("permalink") or "")
    if not url and post_id and (handle := _author_handle(raw)):
        url = f"https://x.com/{handle}/status/{post_id}"

    metrics = raw.get("public_metrics") or raw.get("metrics") or {}
    return RawSignal(
        well="x",
        discovered_at=utc_now_iso(),
        post_id=post_id,
        post_url=url,
        text=text,
        author_handle=_author_handle(raw),
        author_name=_author_name(raw),
        author_followers=int(_author_followers(raw) or 0),
        like_count=int(metrics.get("like_count") or raw.get("like_count") or 0),
        repost_count=int(
            metrics.get("retweet_count") or metrics.get("repost_count") or raw.get("repost_count") or 0
        ),
        reply_count=int(metrics.get("reply_count") or raw.get("reply_count") or 0),
        quote_count=int(metrics.get("quote_count") or raw.get("quote_count") or 0),
        bookmark_count=int(metrics.get("bookmark_count") or raw.get("bookmark_count") or 0),
        created_at=str(raw.get("created_at") or raw.get("createdAt") or ""),
        language=str(raw.get("lang") or raw.get("language") or "en"),
        avatar_id=avatar_id,
        search_theme=search_theme,
        raw_payload=raw,
    )


def _author_handle(raw: dict[str, Any]) -> str:
    a = raw.get("author") or {}
    if isinstance(a, dict):
        return str(a.get("username") or a.get("handle") or raw.get("author_handle") or "")
    if isinstance(a, str):
        return a
    return str(raw.get("author_handle") or "")


def _author_name(raw: dict[str, Any]) -> str:
    a = raw.get("author") or {}
    if isinstance(a, dict):
        return str(a.get("name") or a.get("display_name") or "")
    return ""


def _author_followers(raw: dict[str, Any]) -> int:
    a = raw.get("author") or {}
    if isinstance(a, dict):
        return int(a.get("followers") or a.get("followers_count") or 0)
    return int(raw.get("author_followers") or 0)


def normalize_x_batch(
    raw_posts: list[dict[str, Any]],
    avatar_id: str,
    search_theme: str,
) -> list[RawSignal]:
    out: list[RawSignal] = []
    for raw in raw_posts:
        sig = normalize_x_result(raw, avatar_id, search_theme)
        if sig is not None:
            out.append(sig)
    return out
