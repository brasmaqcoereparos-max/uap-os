from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.enums import (
    WidgetType,
)


@dataclass
class UIWidgetCreationRequest:
    screen_id: str

    widget_type: WidgetType

    name: str | None = None

    x: float = 0
    y: float = 0

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    style: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "screen_id": (
                self.screen_id
            ),
            "widget_type": (
                self.widget_type.value
            ),
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "properties": dict(
                self.properties
            ),
            "style": dict(
                self.style
            ),
  }
