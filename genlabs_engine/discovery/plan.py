"""Build query plans for each discovery well.

The plan is just a list of (avatar_id, theme, query_string) tuples. The
caller (a Hermes skill, a manual CLI, a cron) iterates the plan and
invokes the appropriate discovery tool (x_search / web_search / youtube
search / browser) for each row.

Keeping plan generation Python-only means the skill prompts stay tiny
and we can unit-test the plan logic without Hermes runtime.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

from ..avatars import AvatarRegistry


@dataclass
class XSearchQuery:
    avatar_id: str
    theme: str
    query: str
    min_likes: int = 25
    max_results: int = 20
    lookback_hours: int = 72


def build_x_queries(
    registry: AvatarRegistry,
    *,
    min_likes: int = 25,
    max_results: int = 20,
    lookback_hours: int = 72,
    avatar_filter: list[str] | None = None,
) -> list[XSearchQuery]:
    """Generate one XSearchQuery per (avatar, theme) pair.

    avatar_filter: if provided, only include these avatar ids.
    """
    out: list[XSearchQuery] = []
    for avatar in registry:
        if avatar_filter and avatar.id not in avatar_filter:
            continue
        for theme in avatar.x_search_themes:
            out.append(
                XSearchQuery(
                    avatar_id=avatar.id,
                    theme=theme,
                    query=f'({theme}) min_faves:{min_likes} -is:retweet lang:en',
                    min_likes=min_likes,
                    max_results=max_results,
                    lookback_hours=lookback_hours,
                )
            )
    return out


def plan_as_jsonl_strings(plan: list[XSearchQuery]) -> list[str]:
    import json
    return [json.dumps(asdict(q), ensure_ascii=False) for q in plan]


def plan_summary(plan: list[XSearchQuery]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for q in plan:
        counts[q.avatar_id] = counts.get(q.avatar_id, 0) + 1
    return counts
