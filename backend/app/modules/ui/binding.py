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

    def apply(
        self,
        widget: UIWidget,
        state: UIState,
    ):
        value = state.get(
            self.state_key,
            self.default,
        )

        if self.property_name == "value":
            widget.set_value(value)

        elif self.property_name == "visible":
            widget.visible = bool(value)

        elif self.property_name == "enabled":
            widget.enabled = bool(value)

        else:
            widget.set_property(
                self.property_name,
                value,
            )

        return value
