from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIBreakpoint:
    name: str

    min_width: int = 0
    max_width: int | None = None

    properties: dict[str, Any] = field(
        default_factory=dict
    )

    def matches(
        self,
        width: int,
    ) -> bool:
        if width < self.min_width:
            return False

        if (
            self.max_width is not None
            and width > self.max_width
        ):
            return False

        return True

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "min_width": self.min_width,
            "max_width": self.max_width,
            "properties": dict(
                self.properties
            ),
        }


class UIResponsiveManager:

    def __init__(self) -> None:
        self.breakpoints: list[
            UIBreakpoint
        ] = []

        self._install_defaults()

    def _install_defaults(self) -> None:
        self.breakpoints = [
            UIBreakpoint(
                name="mobile",
                min_width=0,
                max_width=767,
                properties={
                    "columns": 4,
                    "compact": True,
                    "touch": True,
                },
            ),
            UIBreakpoint(
                name="tablet",
                min_width=768,
                max_width=1023,
                properties={
                    "columns": 8,
                    "compact": False,
                    "touch": True,
                },
            ),
            UIBreakpoint(
                name="desktop",
                min_width=1024,
                properties={
                    "columns": 12,
                    "compact": False,
                    "touch": False,
                },
            ),
        ]

    def register(
        self,
        breakpoint: UIBreakpoint,
    ) -> UIBreakpoint:
        self.remove(
            breakpoint.name
        )

        self.breakpoints.append(
            breakpoint
        )

        self.breakpoints.sort(
            key=lambda item: (
                item.min_width
            )
        )

        return breakpoint

    def get(
        self,
        name: str,
    ) -> UIBreakpoint | None:
        for breakpoint in self.breakpoints:
            if breakpoint.name == name:
                return breakpoint

        return None

    def remove(
        self,
        name: str,
    ) -> bool:
        breakpoint = self.get(
            name
        )

        if breakpoint is None:
            return False

        self.breakpoints.remove(
            breakpoint
        )

        return True

    def resolve(
        self,
        width: int,
    ) -> UIBreakpoint | None:
        width = max(
            0,
            int(width),
        )

        for breakpoint in self.breakpoints:
            if breakpoint.matches(
                width
            ):
                return breakpoint

        return None

    def properties_for(
        self,
        width: int,
    ) -> dict[str, Any]:
        breakpoint = self.resolve(
            width
        )

        if breakpoint is None:
            return {}

        return dict(
            breakpoint.properties
        )

    def list_all(
        self,
    ) -> list[UIBreakpoint]:
        return list(
            self.breakpoints
        )


ui_responsive_manager = (
    UIResponsiveManager()
            )
