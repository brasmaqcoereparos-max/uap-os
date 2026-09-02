from typing import Any

from app.modules.ui.command_registry import (
    ui_command_registry,
)
from app.modules.ui.shortcut_manager import (
    ui_shortcut_manager,
)


class UICommandDispatcher:

    def dispatch(
        self,
        command_id: str,
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        return (
            ui_command_registry.execute(
                command_id,
                parameters,
            )
        )

    def dispatch_shortcut(
        self,
        key: str,
        modifiers: list[str],
    ):
        shortcut = (
            ui_shortcut_manager.resolve(
                key,
                modifiers,
            )
        )

        if not shortcut:
            return None

        return self.dispatch(
            shortcut.command,
            shortcut.parameters,
        )


ui_command_dispatcher = (
    UICommandDispatcher()
)
