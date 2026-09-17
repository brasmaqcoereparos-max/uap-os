from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.modules.ui.state import (
    UIState,
)
from app.modules.ui.widget import (
    UIWidget,
)


@dataclass
class UIBinding:
    id: str
    widget_id: str
    property_name: str
    state_key: str

    default: Any = None

    enabled: bool = True

    def apply(
        self,
        widget: UIWidget,
        state: UIState,
    ):
        if not self.enabled:
            return None

        value = state.get(
            self.state_key,
            self.default,
        )

        if (
            self.property_name
            == "value"
        ):
            widget.set_value(
                value
            )

        elif (
            self.property_name
            == "visible"
        ):
            widget.visible = bool(
                value
            )

        elif (
            self.property_name
            == "enabled"
        ):
            widget.enabled = bool(
                value
            )

        elif hasattr(
            widget,
            self.property_name,
        ):
            setattr(
                widget,
                self.property_name,
                value,
            )

        else:
            widget.set_property(
                self.property_name,
                value,
            )

        return value

    def write_back(
        self,
        widget: UIWidget,
        state: UIState,
    ):
        if not self.enabled:
            return None

        if (
            self.property_name
            == "value"
        ):
            value = widget.value

        elif hasattr(
            widget,
            self.property_name,
        ):
            value = getattr(
                widget,
                self.property_name,
            )

        else:
            value = (
                widget.properties.get(
                    self.property_name
                )
            )

        state.set(
            self.state_key,
            value,
        )

        return value

    def to_dict(self):
        return {
            "id": self.id,
            "widget_id": (
                self.widget_id
            ),
            "property_name": (
                self.property_name
            ),
            "state_key": (
                self.state_key
            ),
            "default": self.default,
            "enabled": self.enabled,
        }
