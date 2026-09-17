from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.enums import (
    ScreenType,
)
from app.modules.ui.layout import (
    UILayout,
)


@dataclass
class UIScreen:
    id: str
    name: str

    title: str = ""

    screen_type: ScreenType = (
        ScreenType.STANDARD
    )

    route: str = "/"

    layout: UILayout | None = None

    visible: bool = True

    enabled: bool = True

    requires_auth: bool = False

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    properties: dict[str, Any] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError(
                "Screen id cannot be empty"
            )

        if not self.name:
            raise ValueError(
                "Screen name cannot be empty"
            )

        if not self.route:
            self.route = "/"

        if not self.route.startswith("/"):
            self.route = (
                "/"
                + self.route
            )

    def set_layout(
        self,
        layout: UILayout,
    ):
        self.layout = layout

        return layout

    def set_route(
        self,
        route: str,
    ) -> str:
        route = str(
            route
        ).strip()

        if not route:
            route = "/"

        if not route.startswith("/"):
            route = "/" + route

        self.route = route

        return self.route

    def show(self) -> None:
        self.visible = True

    def hide(self) -> None:
        self.visible = False

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def can_open(
        self,
        authenticated: bool = True,
    ) -> bool:
        if not self.enabled:
            return False

        if (
            self.requires_auth
            and not authenticated
        ):
            return False

        return True

    def set_property(
        self,
        key: str,
        value: Any,
    ) -> Any:
        self.properties[key] = value

        return value

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> Any:
        self.metadata[key] = value

        return value

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "screen_type": (
                self.screen_type.value
            ),
            "route": self.route,
            "visible": self.visible,
            "enabled": self.enabled,
            "requires_auth": (
                self.requires_auth
            ),
            "metadata": dict(
                self.metadata
            ),
            "properties": dict(
                self.properties
            ),
            "layout": (
                self.layout.to_dict()
                if self.layout
                else None
            ),
        }
