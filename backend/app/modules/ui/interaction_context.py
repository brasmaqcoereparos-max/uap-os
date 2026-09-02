from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.interaction_mode import (
    UIInteractionMode,
)


@dataclass
class UIInteractionContext:
    screen_id: str | None = None

    mode: UIInteractionMode = field(
        default_factory=(
            UIInteractionMode
        )
    )

    pointer_x: float = 0
    pointer_y: float = 0

    zoom: float = 1.0

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def set_pointer(
        self,
        x: float,
        y: float,
    ):
        self.pointer_x = x
        self.pointer_y = y

        return (
            self.pointer_x,
            self.pointer_y,
        )

    def set_zoom(
        self,
        zoom: float,
    ):
        self.zoom = max(
            0.1,
            min(
                5.0,
                float(zoom),
            ),
        )

        return self.zoom

    def to_dict(self):
        return {
            "screen_id": (
                self.screen_id
            ),
            "mode": (
                self.mode.to_dict()
            ),
            "pointer_x": (
                self.pointer_x
            ),
            "pointer_y": (
                self.pointer_y
            ),
            "zoom": self.zoom,
            "metadata": dict(
                self.metadata
            ),
      }
