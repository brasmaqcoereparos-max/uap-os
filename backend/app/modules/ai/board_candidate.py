from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIBoardCandidate:
    id: str
    name: str

    score: float = 0.0

    compatible: bool = True

    reasons: list[str] = field(
        default_factory=list
    )

    limitations: list[str] = field(
        default_factory=list
    )

    capabilities: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "score": self.score,
            "compatible": (
                self.compatible
            ),
            "reasons": list(
                self.reasons
            ),
            "limitations": list(
                self.limitations
            ),
            "capabilities": dict(
                self.capabilities
            ),
        }
