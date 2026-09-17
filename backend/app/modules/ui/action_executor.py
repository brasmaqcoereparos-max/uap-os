from __future__ import annotations

from typing import Any

from app.modules.ui.command_dispatcher import (
    ui_command_dispatcher,
)
from app.modules.ui.dialog_manager import (
    ui_dialog_manager,
)
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
        payload: (
            dict[str, Any] | None
        ) = None,
    ):
        payload = dict(
            payload or {}
        )

        action_type = (
            widget.action_type
        )

        action = dict(
            widget.action or {}
        )

        if (
            action_type
            == ActionType.NONE
        ):
            return {
                "executed": False,
                "reason": "no_action",
            }

        if (
            action_type
            == ActionType.NAVIGATE
        ):
            screen_id = (
                action.get(
                    "screen_id"
                )
            )

            if not screen_id:
                raise ValueError(
                    "screen_id is required"
                )

            screen = (
                ui_navigation.navigate(
                    screen_id
                )
            )

            return {
                "executed": True,
                "action": "navigate",
                "screen_id": (
                    screen.id
                ),
            }

        if (
            action_type
            == ActionType.SET_VALUE
        ):
            key = action.get(
                "key"
            )

            if not key:
                raise ValueError(
                    "state key is required"
                )

            value = (
                payload.get(
                    "value",
                    action.get(
                        "value"
                    ),
                )
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

        if (
            action_type
            == ActionType.COMMAND
        ):
            command_id = (
                action.get(
                    "command_id"
                )
                or action.get(
                    "command"
                )
            )

            if not command_id:
                raise ValueError(
                    "command_id is required"
                )

            parameters = dict(
                action.get(
                    "parameters",
                    {},
                )
            )

            parameters.update(
                payload
            )

            result = (
                ui_command_dispatcher
                .dispatch(
                    command_id,
                    parameters,
                )
            )

            return {
                "executed": True,
                "action": "command",
                "command_id": (
                    command_id
                ),
                "result": result,
            }

        if (
            action_type
            == ActionType.OPEN_DIALOG
        ):
            dialog_id = (
                action.get(
                    "dialog_id"
                )
            )

            if not dialog_id:
                raise ValueError(
                    "dialog_id is required"
                )

            data = dict(
                action.get(
                    "data",
                    {},
                )
            )

            data.update(
                payload
            )

            dialog = (
                ui_dialog_manager.open(
                    dialog_id,
                    data,
                )
            )

            return {
                "executed": True,
                "action": (
                    "open_dialog"
                ),
                "dialog_id": (
                    dialog.id
                ),
            }

        if (
            action_type
            == ActionType.CLOSE_DIALOG
        ):
            dialog_id = (
                action.get(
                    "dialog_id"
                )
            )

            if dialog_id:
                closed = (
                    ui_dialog_manager
                    .close(
                        dialog_id
                    )
                )

                return {
                    "executed": (
                        bool(closed)
                    ),
                    "action": (
                        "close_dialog"
                    ),
                    "dialog_id": (
                        dialog_id
                    ),
                }

            dialog = (
                ui_dialog_manager
                .close_top()
            )

            return {
                "executed": (
                    dialog is not None
                ),
                "action": (
                    "close_dialog"
                ),
                "dialog_id": (
                    dialog.id
                    if dialog
                    else None
                ),
            }

        if (
            action_type
            == ActionType.AUTOMATION
        ):
            return {
                "executed": False,
                "action": "automation",
                "reason": (
                    "runtime_bridge_required"
                ),
                "payload": payload,
                "configuration": (
                    action
                ),
            }

        raise ValueError(
            "Unsupported action type: "
            f"{action_type}"
        )


ui_action_executor = (
    UIActionExecutor()
)
