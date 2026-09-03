from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIUIIntent:
    text: str

    app_type: str = "general"

    preferences: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    confidence: float = 0.0

    def to_dict(self):
        return {
            "text": self.text,
            "app_type": self.app_type,
            "preferences": dict(
                self.preferences
            ),
            "confidence": (
                self.confidence
            ),
        }
