from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.enums import (
    ActionType,
    WidgetType,
)


@dataclass
class UIWidget:
    id: str
    name: str
    widget_type: WidgetType

    x: float = 0
    y: float = 0

    width: float = 100
    height: float = 40

    visible: bool = True
    enabled: bool = True

    value: Any = None

    properties: dict[str, Any] = field(
        default_factory=dict
    )

    style: dict[str, Any] = field(
        default_factory=dict
    )

    action_type: ActionType = (
        ActionType.NONE
    )

    action: dict[str, Any] = field(
        default_factory=dict
    )

    def set_value(
        self,
        value: Any,
    ):
        self.value = value

        return self.value

    def set_property(
        self,
        key: str,
        value: Any,
    ):
        self.properties[key] = value

        return value

    def set_style(
        self,
        key: str,
        value: Any,
    ):
        self.style[key] = value

        return value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "widget_type": (
                self.widget_type.value
            ),
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "visible": self.visible,
            "enabled": self.enabled,
            "value": self.value,
            "properties": dict(
                self.properties
            ),
            "style": dict(self.style),
            "action_type": (
                self.action_type.value
            ),
            "action": dict(self.action),
  }
