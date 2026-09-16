from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from app.modules.ui.dock_manager import (
    ui_dock_manager,
)


@dataclass
class UIStudioLayout:
    name: str = "default"

    toolbar_visible: bool = True
    statusbar_visible: bool = True

    user_level: str = "beginner"

    dock_state: dict = field(
        default_factory=dict
    )

    def capture(self):
        self.dock_state = (
            ui_dock_manager.snapshot()
        )

        return self.dock_state

    def apply_user_level(
        self,
        level: str,
    ) -> str:
        normalized = str(
            level
        ).strip().lower()

        if normalized not in {
            "beginner",
            "intermediate",
            "professional",
        }:
            raise ValueError(
                f"Unsupported studio level: {level}"
            )

        self.user_level = normalized

        if normalized == "beginner":
            self.toolbar_visible = True
            self.statusbar_visible = False

        elif normalized == "intermediate":
            self.toolbar_visible = True
            self.statusbar_visible = True

        else:
            self.toolbar_visible = True
            self.statusbar_visible = True

        return self.user_level

    def set_toolbar_visible(
        self,
        visible: bool,
    ) -> bool:
        self.toolbar_visible = bool(
            visible
        )

        return self.toolbar_visible

    def set_statusbar_visible(
        self,
        visible: bool,
    ) -> bool:
        self.statusbar_visible = bool(
            visible
        )

        return self.statusbar_visible

    def to_dict(self):
        return {
            "name": self.name,
            "toolbar_visible": (
                self.toolbar_visible
            ),
            "statusbar_visible": (
                self.statusbar_visible
            ),
            "user_level": (
                self.user_level
            ),
            "dock_state": dict(
                self.dock_state
            ),
        }
