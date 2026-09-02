from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIPage:
    id: str
    name: str

    screen_id: str

    order: int = 0

    enabled: bool = True

    icon: str | None = None

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "screen_id": self.screen_id,
            "order": self.order,
            "enabled": self.enabled,
            "icon": self.icon,
            "properties": dict(
                self.properties
            ),
        }
