from dataclasses import dataclass, field
from typing import Any


@dataclass
class AIResult:

    model: str
    detections: list[Any] = field(
        default_factory=list
    )

    success: bool = True
    error: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):

        return {
            "model": self.model,
            "detections": list(
                self.detections
            ),
            "success": self.success,
            "error": self.error,
            "metadata": dict(
                self.metadata
            ),
        }

    @property
    def count(self):

        return len(
            self.detections
        )
