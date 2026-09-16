from __future__ import annotations

from app.modules.ui.dashboard import (
    UIDashboard,
)


class UIDashboardRegistry:

    def __init__(self):
        self._dashboards: dict[
            str,
            UIDashboard,
        ] = {}

    def register(
        self,
        dashboard: UIDashboard,
    ):
        self._dashboards[
            dashboard.id
        ] = dashboard

        return dashboard

    def create(
        self,
        dashboard_id: str,
        name: str,
        columns: int = 12,
    ) -> UIDashboard:
        if dashboard_id in self._dashboards:
            raise ValueError(
                "Dashboard already exists: "
                f"{dashboard_id}"
            )

        dashboard = UIDashboard(
            id=dashboard_id,
            name=name,
            columns=columns,
        )

        return self.register(
            dashboard
        )

    def get(
        self,
        dashboard_id: str,
    ):
        return self._dashboards.get(
            dashboard_id
        )

    def require(
        self,
        dashboard_id: str,
    ) -> UIDashboard:
        dashboard = self.get(
            dashboard_id
        )

        if dashboard is None:
            raise KeyError(
                "Dashboard not found: "
                f"{dashboard_id}"
            )

        return dashboard

    def remove(
        self,
        dashboard_id: str,
    ):
        return self._dashboards.pop(
            dashboard_id,
            None,
        )

    def list_all(self):
        return list(
            self._dashboards.values()
        )

    def snapshot(self) -> list[dict]:
        return [
            dashboard.to_dict()
            for dashboard
            in self.list_all()
        ]

    def clear(self):
        self._dashboards.clear()


ui_dashboard_registry = (
    UIDashboardRegistry()
        )
