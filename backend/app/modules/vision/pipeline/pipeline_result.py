from dataclasses import dataclass, field
from typing import Any


@dataclass
class PipelineResult:

    camera_id: str | None = None

    analysis: dict[str, Any] = field(
        default_factory=dict
    )

    events: list[Any] = field(
        default_factory=list
    )

    decisions: list[Any] = field(
        default_factory=list
    )

    actions: list[Any] = field(
        default_factory=list
    )

    success: bool = True

    error: str | None = None

    def to_dict(self):

        return {
            "camera_id": self.camera_id,
            "analysis": dict(self.analysis),
            "events": list(self.events),
            "decisions": list(self.decisions),
            "actions": list(self.actions),
            "success": self.success,
            "error": self.error,
        }
