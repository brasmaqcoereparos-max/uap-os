from __future__ import annotations

from app.modules.monitoring.diagnostic_service import (
    monitoring_diagnostic_service,
)
from app.modules.monitoring.status import (
    monitoring_status,
)
from app.modules.monitoring.system_health_service import (
    monitoring_system_health_service,
)


class MonitoringFacade:

    def report_module(
        self,
        module: str,
        healthy: bool,
        details: dict | None = None,
    ):

        result = (
            monitoring_system_health_service
            .report(
                module=module,
                healthy=healthy,
                details=details,
            )
        )

        return result.to_dict()

    def report_metrics(
        self,
        machine_id: str,
        *,
        planned_time_seconds: (
            float | None
        ) = None,
        ideal_cycle_seconds: (
            float | None
        ) = None,
    ):

        from app.modules.metrics.monitoring_bridge import (
            metrics_monitoring_bridge,
        )

        return (
            metrics_monitoring_bridge
            .report_machine(
                machine_id,
                planned_time_seconds=(
                    planned_time_seconds
                ),
                ideal_cycle_seconds=(
                    ideal_cycle_seconds
                ),
            )
        )

    def machine_metrics(
        self,
        machine_id: str,
    ):

        from app.modules.metrics.metrics_service import (
            metrics_service,
        )

        return (
            metrics_service
            .machine_snapshot(
                machine_id
            )
        )

    def diagnose(self):

        return (
            monitoring_diagnostic_service
            .run()
            .to_dict()
        )

    def status(self):

        return (
            monitoring_status
            .snapshot()
        )


monitoring_facade = (
    MonitoringFacade()
)
