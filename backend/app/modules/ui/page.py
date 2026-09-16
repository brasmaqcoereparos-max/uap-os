from __future__ import annotations

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

    def __post_init__(self) -> None:
        self.order = int(
            self.order
        )

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def set_order(
        self,
        order: int,
    ) -> int:
        self.order = int(
            order
        )

        return self.order

    def set_screen(
        self,
        screen_id: str,
    ) -> str:
        if not screen_id:
            raise ValueError(
                "screen_id cannot be empty"
            )

        self.screen_id = screen_id

        return self.screen_id

    def set_property(
        self,
        key: str,
        value: Any,
    ) -> Any:
        self.properties[key] = value

        return value

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
