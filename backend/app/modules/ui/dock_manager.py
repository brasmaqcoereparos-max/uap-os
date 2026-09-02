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

    def dock(
        self,
        panel_id: str,
        position: str,
    ):
        target = self.area(
            position
        )

        if not target:
            raise ValueError(
                "Invalid dock position: "
                f"{position}"
            )

        self.undock(panel_id)

        target.add(panel_id)

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

    def locate(
        self,
        panel_id: str,
    ):
        for (
            position,
            area,
        ) in self._areas.items():
            if (
                panel_id
                in area.panel_ids
            ):
                return position

        return None

    def snapshot(self):
        return {
            position: area.to_dict()
            for position, area
            in self._areas.items()
        }


ui_dock_manager = UIDockManager()
