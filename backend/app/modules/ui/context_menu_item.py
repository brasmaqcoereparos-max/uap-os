from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIContextMenuItem:
    id: str
    label: str

    command: str | None = None
    icon: str | None = None

    separator: bool = False

    enabled: bool = True
    visible: bool = True

    order: int = 0

    parameters: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "command": self.command,
            "icon": self.icon,
            "separator": self.separator,
            "enabled": self.enabled,
            "visible": self.visible,
            "order": self.order,
            "parameters": dict(
                self.parameters
            ),
        }
