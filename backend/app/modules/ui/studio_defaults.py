from app.modules.ui.dock_manager import (
    ui_dock_manager,
)
from app.modules.ui.panel import (
    UIPanel,
)
from app.modules.ui.panel_registry import (
    ui_panel_registry,
)


class UIStudioDefaults:

    @staticmethod
    def install():
        panels = [
            UIPanel(
                id="palette",
                name="Palette",
                title="Components",
                position="left",
                width=280,
                order=10,
            ),
            UIPanel(
                id="hierarchy",
                name="Hierarchy",
                title="Hierarchy",
                position="left",
                width=280,
                order=20,
            ),
            UIPanel(
                id="properties",
                name="Properties",
                title="Properties",
                position="right",
                width=320,
                order=10,
            ),
            UIPanel(
                id="events",
                name="Events",
                title="Events",
                position="right",
                width=320,
                order=20,
            ),
            UIPanel(
                id="console",
                name="Console",
                title="Console",
                position="bottom",
                height=220,
                order=10,
            ),
            UIPanel(
                id="preview",
                name="Preview",
                title="Preview",
                position="center",
                order=10,
            ),
        ]

        for panel in panels:
            ui_panel_registry.register(
                panel
            )

            ui_dock_manager.dock(
                panel.id,
                panel.position,
            )

        return panels


def install_studio_defaults():
    return UIStudioDefaults.install()
