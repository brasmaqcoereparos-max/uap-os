from dataclasses import dataclass, field
from typing import Any


@dataclass
class PipelineContext:

    camera_id: str | None = None

    frame: Any = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

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

    def update(
        self,
        **values,
    ):

        for key, value in values.items():

            if hasattr(
                self,
                key,
            ):
                setattr(
                    self,
                    key,
                    value,
                )

        return self

    def to_dict(self):

        return {
            "camera_id": self.camera_id,
            "metadata": dict(self.metadata),
            "analysis": dict(self.analysis),
            "events": list(self.events),
            "decisions": list(self.decisions),
            "actions": list(self.actions),
        }
