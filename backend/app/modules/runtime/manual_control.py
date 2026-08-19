from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ManualCommand:
    target: str
    action: str
    value: Any = None
    source: str = "manual"


class ManualControlManager:
    """
    Camada comum para controle manual através de
    joystick, teclado, mouse, touchscreen ou interface gráfica.
    """

    def __init__(self) -> None:
        self._commands: list[ManualCommand] = []
        self.enabled = True

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def command(
        self,
        target: str,
        action: str,
        value: Any = None,
        source: str = "manual",
    ) -> ManualCommand:
        if not self.enabled:
            raise RuntimeError(
                "Manual control is disabled"
            )

        command = ManualCommand(
            target=target,
            action=action,
            value=value,
            source=source,
        )

        self._commands.append(command)

        return command

    def history(self) -> list[ManualCommand]:
        return list(self._commands)

    def clear_history(self) -> None:
        self._commands.clear()

    def last_command(self) -> ManualCommand | None:
        if not self._commands:
            return None

        return self._commands[-1]
