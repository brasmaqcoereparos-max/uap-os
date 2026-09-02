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

    dock_state: dict = field(
        default_factory=dict
    )

    def capture(self):
        self.dock_state = (
            ui_dock_manager.snapshot()
        )

        return self.dock_state

    def to_dict(self):
        return {
            "name": self.name,
            "toolbar_visible": (
                self.toolbar_visible
            ),
            "statusbar_visible": (
                self.statusbar_visible
            ),
            "dock_state": dict(
                self.dock_state
            ),
        }
