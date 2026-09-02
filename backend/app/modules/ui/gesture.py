from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIGesture:
    gesture_type: str

    target_id: str | None = None

    start_x: float | None = None
    start_y: float | None = None

    current_x: float | None = None
    current_y: float | None = None

    delta_x: float = 0
    delta_y: float = 0

    scale: float = 1.0
    rotation: float = 0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "gesture_type": (
                self.gesture_type
            ),
            "target_id": (
                self.target_id
            ),
            "start_x": self.start_x,
            "start_y": self.start_y,
            "current_x": (
                self.current_x
            ),
            "current_y": (
                self.current_y
            ),
            "delta_x": self.delta_x,
            "delta_y": self.delta_y,
            "scale": self.scale,
            "rotation": (
                self.rotation
            ),
            "metadata": dict(
                self.metadata
            ),
      }
