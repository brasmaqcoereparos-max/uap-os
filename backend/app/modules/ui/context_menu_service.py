from typing import Any

from app.modules.ui.command_dispatcher import (
    ui_command_dispatcher,
)
from app.modules.ui.context_menu_registry import (
    ui_context_menu_registry,
)


class UIContextMenuService:

    def open(
        self,
        menu_id: str,
        context: (
            dict[str, Any] | None
        ) = None,
    ):
        menu = (
            ui_context_menu_registry
            .get(menu_id)
        )

        if not menu:
            raise ValueError(
                "Context menu not found: "
                f"{menu_id}"
            )

        return {
            "menu": menu.to_dict(),
            "context": dict(
                context or {}
            ),
        }

    def execute(
        self,
        menu_id: str,
        item_id: str,
        context: (
            dict[str, Any] | None
        ) = None,
    ):
        menu = (
            ui_context_menu_registry
            .get(menu_id)
        )

        if not menu:
            raise ValueError(
                "Context menu not found: "
                f"{menu_id}"
            )

        item = menu.get(
            item_id
        )

        if (
            not item
            or not item.visible
        ):
            raise ValueError(
                "Context menu item "
                "not found"
            )

        if not item.enabled:
            return None

        if (
            item.separator
            or not item.command
        ):
            return None

        parameters = dict(
            item.parameters
        )

        parameters.update(
            context or {}
        )

        return (
            ui_command_dispatcher
            .dispatch(
                item.command,
                parameters,
            )
        )


ui_context_menu_service = (
    UIContextMenuService()
)
