"""GenLabs Thai SME content engine.

Layered architecture (bottom-up):

    1. avatars      — who we serve (Thai services SMEs)
    2. discovery    — wells we mine (x, web, youtube, voice)
    3. ideation     — avatar-aware idea minting + novelty
    4. concept      — concept studio + judge
    5. production   — format-aware rendering
    6. distribution — Zernio draft + manual publish gate
    7. measurement  — performance attribution by avatar/format/hook
    8. learning     — nightly mutation of state files
"""
from __future__ import annotations

__version__ = "0.1.0"

__all__ = [
    "__version__",
]
