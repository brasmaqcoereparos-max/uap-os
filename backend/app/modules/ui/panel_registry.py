from __future__ import annotations

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

    def require(
        self,
        panel_id: str,
    ) -> UIPanel:
        panel = self.get(
            panel_id
        )

        if panel is None:
            raise KeyError(
                f"Panel not found: {panel_id}"
            )

        return panel

    def remove(
        self,
        panel_id: str,
    ):
        return self._panels.pop(
            panel_id,
            None,
        )

    def show(
        self,
        panel_id: str,
    ) -> bool:
        panel = self.get(
            panel_id
        )

        if panel is None:
            return False

        panel.show()

        return True

    def hide(
        self,
        panel_id: str,
    ) -> bool:
        panel = self.get(
            panel_id
        )

        if panel is None:
            return False

        panel.hide()

        return True

    def collapse(
        self,
        panel_id: str,
    ) -> bool:
        panel = self.get(
            panel_id
        )

        if panel is None:
            return False

        panel.collapse()

        return True

    def expand(
        self,
        panel_id: str,
    ) -> bool:
        panel = self.get(
            panel_id
        )

        if panel is None:
            return False

        panel.expand()

        return True

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
                for panel
                in panels
                if panel.visible
            ]

        return sorted(
            panels,
            key=lambda panel: (
                panel.order,
                panel.name,
            ),
        )

    def by_position(
        self,
        position: str,
    ) -> list[UIPanel]:
        return [
            panel
            for panel
            in self.list_all()
            if panel.position
            == position
        ]

    def snapshot(self) -> list[dict]:
        return [
            panel.to_dict()
            for panel
            in self.list_all()
        ]

    def clear(self):
        self._panels.clear()


ui_panel_registry = (
    UIPanelRegistry()
)
