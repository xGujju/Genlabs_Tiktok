"""Avatar registry — loads /config/avatars/*.yaml.

Single source of truth for who the engine serves. Read by ideation,
concept, production, learning layers.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AVATARS_DIR = REPO_ROOT / "config" / "avatars"


@dataclass
class Avatar:
    id: str
    display_name: str
    industry: str
    subindustry: str
    status: str
    priority: int
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_yaml(cls, path: Path) -> "Avatar":
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or "id" not in data:
            raise ValueError(f"invalid avatar file (missing id): {path}")
        return cls(
            id=str(data["id"]),
            display_name=str(data.get("display_name", data["id"])),
            industry=str(data.get("industry", "")),
            subindustry=str(data.get("subindustry", "")),
            status=str(data.get("status", "draft")),
            priority=int(data.get("priority", 99)),
            raw=data,
        )

    # ---- convenience accessors (read raw at call site if you need more) ----

    @property
    def x_search_themes(self) -> list[str]:
        return list(self.raw.get("search_seeds_for_discovery", {}).get("x_search_themes", []) or [])

    @property
    def web_search_themes(self) -> list[str]:
        return list(self.raw.get("search_seeds_for_discovery", {}).get("web_search_themes", []) or [])

    @property
    def youtube_search_themes(self) -> list[str]:
        return list(self.raw.get("search_seeds_for_discovery", {}).get("youtube_search_themes", []) or [])

    @property
    def daily_pains(self) -> list[dict[str, Any]]:
        return list(self.raw.get("daily_pains", []) or [])

    @property
    def weekly_pains(self) -> list[dict[str, Any]]:
        return list(self.raw.get("weekly_pains", []) or [])

    @property
    def format_affinity_ranked(self) -> list[str]:
        return list(self.raw.get("content_preferences", {}).get("format_affinity_ranked", []) or [])

    @property
    def hook_frame_affinity_ranked(self) -> list[str]:
        return list(self.raw.get("content_preferences", {}).get("hook_frame_affinity_ranked", []) or [])

    @property
    def voice_register(self) -> str:
        return str(self.raw.get("voice_register", {}).get("default", "warm_friend"))

    @property
    def locked_phrases(self) -> list[str]:
        return list(self.raw.get("locked_phrases_native_feel", []) or [])

    @property
    def avoid_phrases(self) -> list[str]:
        return list(self.raw.get("avoid_phrases_foreign_feel", []) or [])


@dataclass
class AvatarRegistry:
    avatars: dict[str, Avatar]
    variety_rules: dict[str, Any]
    weekly_format_mix: dict[str, float]
    weekly_hook_mix: dict[str, float]
    schema_version: int = 1

    @classmethod
    def load(cls, avatars_dir: Path | None = None) -> "AvatarRegistry":
        avatars_dir = avatars_dir or DEFAULT_AVATARS_DIR
        index_path = avatars_dir / "_index.yaml"
        if not index_path.exists():
            raise FileNotFoundError(f"avatar index not found: {index_path}")
        idx = yaml.safe_load(index_path.read_text(encoding="utf-8")) or {}
        avatars: dict[str, Avatar] = {}
        for entry in idx.get("avatars", []) or []:
            f = avatars_dir / entry["file"]
            avatar = Avatar.from_yaml(f)
            avatars[avatar.id] = avatar
        return cls(
            avatars=avatars,
            variety_rules=idx.get("variety_rules", {}) or {},
            weekly_format_mix=idx.get("weekly_format_mix", {}) or {},
            weekly_hook_mix=idx.get("weekly_hook_mix", {}) or {},
            schema_version=int(idx.get("schema_version", 1)),
        )

    def active(self) -> list[Avatar]:
        return [a for a in self.avatars.values() if a.status == "active"]

    def priority_n(self, n: int) -> list[Avatar]:
        return sorted(
            (a for a in self.avatars.values() if a.priority == n),
            key=lambda a: a.id,
        )

    def __getitem__(self, avatar_id: str) -> Avatar:
        return self.avatars[avatar_id]

    def __iter__(self) -> Iterator[Avatar]:
        return iter(self.avatars.values())

    def __len__(self) -> int:
        return len(self.avatars)

    def __contains__(self, avatar_id: object) -> bool:
        return avatar_id in self.avatars
