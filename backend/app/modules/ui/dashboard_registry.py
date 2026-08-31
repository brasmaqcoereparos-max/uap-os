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

    def get(
        self,
        dashboard_id: str,
    ):
        return self._dashboards.get(
            dashboard_id
        )

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

    def clear(self):
        self._dashboards.clear()


ui_dashboard_registry = (
    UIDashboardRegistry()
      )
