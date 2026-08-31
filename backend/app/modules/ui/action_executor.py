from typing import Any

from app.modules.ui.enums import (
    ActionType,
)
from app.modules.ui.navigation import (
    ui_navigation,
)
from app.modules.ui.state import (
    ui_state,
)
from app.modules.ui.widget import (
    UIWidget,
)


class UIActionExecutor:

    def execute(
        self,
        widget: UIWidget,
        payload: dict[str, Any] | None = None,
    ):
        payload = payload or {}

        action_type = widget.action_type
        action = widget.action

        if action_type == ActionType.NONE:
            return {
                "executed": False,
                "reason": "no_action",
            }

        if action_type == ActionType.NAVIGATE:
            screen_id = action.get(
                "screen_id"
            )

            if not screen_id:
                raise ValueError(
                    "screen_id is required"
                )

            screen = ui_navigation.navigate(
                screen_id
            )

            return {
                "executed": True,
                "action": "navigate",
                "screen_id": screen.id,
            }

        if action_type == ActionType.SET_VALUE:
            key = action.get("key")

            if not key:
                raise ValueError(
                    "state key is required"
                )

            value = payload.get(
                "value",
                action.get("value"),
            )

            ui_state.set(
                key,
                value,
            )

            return {
                "executed": True,
                "action": "set_value",
                "key": key,
                "value": value,
            }

        return {
            "executed": True,
            "action": action_type.value,
            "payload": payload,
            "configuration": dict(
                action
            ),
        }


ui_action_executor = (
    UIActionExecutor()
)
