from typing import Any

from app.modules.ui.command import (
    UICommand,
)


class UICommandRegistry:

    def __init__(self):
        self._commands: dict[
            str,
            UICommand,
        ] = {}

    def register(
        self,
        command: UICommand,
    ):
        self._commands[
            command.id
        ] = command

        return command

    def get(
        self,
        command_id: str,
    ):
        return self._commands.get(
            command_id
        )

    def execute(
        self,
        command_id: str,
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        command = self.get(
            command_id
        )

        if not command:
            raise ValueError(
                "Command not found: "
                f"{command_id}"
            )

        return command.execute(
            parameters
        )

    def remove(
        self,
        command_id: str,
    ):
        return self._commands.pop(
            command_id,
            None,
        )

    def list_all(self):
        return list(
            self._commands.values()
        )

    def clear(self):
        self._commands.clear()


ui_command_registry = (
    UICommandRegistry()
)
