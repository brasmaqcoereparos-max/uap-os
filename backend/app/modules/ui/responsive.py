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
    ):
        if width < self.min_width:
            return False

        if (
            self.max_width is not None
            and width > self.max_width
        ):
            return False

        return True


class UIResponsiveManager:

    def __init__(self):
        self.breakpoints = [
            UIBreakpoint(
                name="mobile",
                min_width=0,
                max_width=767,
            ),
            UIBreakpoint(
                name="tablet",
                min_width=768,
                max_width=1023,
            ),
            UIBreakpoint(
                name="desktop",
                min_width=1024,
            ),
        ]

    def resolve(
        self,
        width: int,
    ):
        for breakpoint in (
            self.breakpoints
        ):
            if breakpoint.matches(width):
                return breakpoint

        return None


ui_responsive_manager = (
    UIResponsiveManager()
      )
