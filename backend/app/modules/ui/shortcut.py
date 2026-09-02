from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIShortcut:
    id: str

    key: str

    command: str

    modifiers: list[str] = field(
        default_factory=list
    )

    enabled: bool = True

    parameters: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def matches(
        self,
        key: str,
        modifiers: list[str],
    ):
        if not self.enabled:
            return False

        if (
            self.key.lower()
            != key.lower()
        ):
            return False

        expected = {
            item.lower()
            for item
            in self.modifiers
        }

        received = {
            item.lower()
            for item
            in modifiers
        }

        return expected == received

    def to_dict(self):
        return {
            "id": self.id,
            "key": self.key,
            "command": self.command,
            "modifiers": list(
                self.modifiers
            ),
            "enabled": self.enabled,
            "parameters": dict(
                self.parameters
            ),
          }
