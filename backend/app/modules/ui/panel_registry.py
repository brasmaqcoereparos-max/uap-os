from app.modules.ui.panel import (
    UIPanel,
)


class UIPanelRegistry:

    def __init__(self):
        self._panels: dict[
            str,
            UIPanel,
        ] = {}

    def register(
        self,
        panel: UIPanel,
    ):
        self._panels[
            panel.id
        ] = panel

        return panel

    def get(
        self,
        panel_id: str,
    ):
        return self._panels.get(
            panel_id
        )

    def remove(
        self,
        panel_id: str,
    ):
        return self._panels.pop(
            panel_id,
            None,
        )

    def list_all(
        self,
        visible_only: bool = False,
    ):
        panels = list(
            self._panels.values()
        )

        if visible_only:
            panels = [
                panel
                for panel in panels
                if panel.visible
            ]

        return sorted(
            panels,
            key=lambda panel: (
                panel.order,
                panel.name,
            ),
        )

    def clear(self):
        self._panels.clear()


ui_panel_registry = (
    UIPanelRegistry()
    )
