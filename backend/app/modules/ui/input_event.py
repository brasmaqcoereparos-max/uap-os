from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIInputEvent:
    event_type: str

    target_id: str | None = None

    x: float | None = None
    y: float | None = None

    key: str | None = None

    value: Any = None

    modifiers: list[str] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "event_type": (
                self.event_type
            ),
            "target_id": self.target_id,
            "x": self.x,
            "y": self.y,
            "key": self.key,
            "value": self.value,
            "modifiers": list(
                self.modifiers
            ),
            "metadata": dict(
                self.metadata
            ),
        }
