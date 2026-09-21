from __future__ import annotations

from app.modules.metrics.alert_service import (
    alert_service,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.oee_service import (
    oee_service,
)
from app.modules.monitoring.system_health_service import (
    monitoring_system_health_service,
)


class MetricsMonitoringBridge:

    def report_machine(
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

        active_faults = (
            fault_service.list(
                machine_id,
                active_only=True,
            )
        )

        active_alerts = (
            alert_service.alerts(
                machine_id,
                active_only=True,
            )
        )

        oee = oee_service.calculate(
            machine_id,
            planned_time_seconds=(
                planned_time_seconds
            ),
            ideal_cycle_seconds=(
                ideal_cycle_seconds
            ),
        )

        critical_alerts = [
            alert
            for alert in active_alerts
            if alert[
                "level"
            ]
            == "critical"
        ]

        critical_faults = [
            fault
            for fault in active_faults
            if fault[
                "severity"
            ]
            == "critical"
        ]

        healthy = not (
            critical_alerts
            or critical_faults
        )

        details = {
            "machine_id": (
                machine_id
            ),
            "active_faults": len(
                active_faults
            ),
            "active_alerts": len(
                active_alerts
            ),
            "critical_faults": len(
                critical_faults
            ),
            "critical_alerts": len(
                critical_alerts
            ),
            "oee_percent": (
                oee[
                    "oee_percent"
                ]
            ),
        }

        module_health = (
            monitoring_system_health_service
            .report(
                module=(
                    f"metrics:{machine_id}"
                ),
                healthy=healthy,
                details=details,
            )
        )

        return {
            "healthy": healthy,
            "details": details,
            "monitoring": (
                module_health.to_dict()
            ),
        }


metrics_monitoring_bridge = (
    MetricsMonitoringBridge()
      )
