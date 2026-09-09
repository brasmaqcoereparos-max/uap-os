from app.modules.monitoring.health_state import (
    MonitoringHealthState,
)
from app.modules.monitoring.module_health import (
    MonitoringModuleHealth,
)
from app.modules.monitoring.module_health_registry import (
    monitoring_module_health_registry,
)
from app.modules.monitoring.system_snapshot import (
    MonitoringSystemSnapshot,
)


class MonitoringSystemHealthService:

    def report(
        self,
        module: str,
        healthy: bool,
        details: dict | None = None,
    ):
        state = (
            MonitoringHealthState.HEALTHY
            if healthy
            else MonitoringHealthState.UNHEALTHY
        )

        health = MonitoringModuleHealth(
            module=module,
            state=state,
            available=True,
            details=dict(
                details or {}
            ),
        )

        return (
            monitoring_module_health_registry
            .register(
                health
            )
        )

    def snapshot(self):
        modules = (
            monitoring_module_health_registry
            .list_all()
        )

        healthy = all(
            item.state
            == MonitoringHealthState.HEALTHY
            for item in modules
        )

        return (
            MonitoringSystemSnapshot(
                healthy=healthy,
                modules=[
                    item.to_dict()
                    for item in modules
                ],
            )
        )


monitoring_system_health_service = (
    MonitoringSystemHealthService()
)
