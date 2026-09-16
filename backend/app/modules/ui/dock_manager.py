from __future__ import annotations

from app.modules.ui.dock_area import (
    UIDockArea,
)


class UIDockManager:

    POSITIONS = (
        "left",
        "right",
        "top",
        "bottom",
        "center",
    )

    def __init__(self):
        self._areas = {
            position: UIDockArea(
                position=position
            )
            for position
            in self.POSITIONS
        }

    def area(
        self,
        position: str,
    ):
        return self._areas.get(
            position
        )

    def require_area(
        self,
        position: str,
    ) -> UIDockArea:
        area = self.area(
            position
        )

        if area is None:
            raise ValueError(
                "Invalid dock position: "
                f"{position}"
            )

        return area

    def dock(
        self,
        panel_id: str,
        position: str,
    ):
        target = self.require_area(
            position
        )

        self.undock(
            panel_id
        )

        target.add(
            panel_id
        )

        return target

    def undock(
        self,
        panel_id: str,
    ):
        removed = False

        for area in (
            self._areas.values()
        ):
            if area.remove(
                panel_id
            ):
                removed = True

        return removed

    def relocate(
        self,
        panel_id: str,
        position: str,
        index: int | None = None,
    ):
        area = self.dock(
            panel_id,
            position,
        )

        if index is not None:
            area.move(
                panel_id,
                index,
            )

        return area

    def activate(
        self,
        panel_id: str,
    ) -> bool:
        position = self.locate(
            panel_id
        )

        if position is None:
            return False

        area = self.area(
            position
        )

        if area is None:
            return False

        return area.activate(
            panel_id
        )

    def locate(
        self,
        panel_id: str,
    ):
        for (
            position,
            area,
        ) in self._areas.items():
            if area.contains(
                panel_id
            ):
                return position

        return None

    def panels(
        self,
        position: str,
    ) -> list[str]:
        area = self.require_area(
            position
        )

        return list(
            area.panel_ids
        )

    def clear(self) -> None:
        for area in (
            self._areas.values()
        ):
            area.clear()

    def snapshot(self):
        return {
            position: area.to_dict()
            for position, area
            in self._areas.items()
        }


ui_dock_manager = UIDockManager()
