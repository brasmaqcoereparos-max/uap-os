from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIAutomationIntent:
    text: str

    objective: str = ""

    entities: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    confidence: float = 0.0

    def to_dict(self):
        return {
            "text": self.text,
            "objective": (
                self.objective
            ),
            "entities": dict(
                self.entities
            ),
            "confidence": (
                self.confidence
            ),
        }
