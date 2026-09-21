from __future__ import annotations

from app.modules.metrics.alert_service import (
    alert_service,
)
from app.modules.metrics.consumption_service import (
    consumption_service,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.metrics.monitoring_bridge import (
    metrics_monitoring_bridge,
)
from app.modules.metrics.oee_service import (
    oee_service,
)
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)


class MetricsService:

    def record_telemetry(
        self,
        name: str,
        value: float,
        *,
        machine_id: str | None = None,
        unit: str = "",
        tags=None,
        metadata=None,
    ):

        point = (
            telemetry_service.record(
                name=name,
                value=value,
                unit=unit,
                source=machine_id,
                tags=tags,
                metadata=metadata,
            )
        )

        metrics_history_service.record(
            "telemetry",
            point.to_dict(),
            source=machine_id,
        )

        alerts = (
            alert_service.evaluate(
                metric=name,
                value=value,
                machine_id=(
                    machine_id
                ),
            )
        )

        return {
            "metric": (
                point.to_dict()
            ),
            "alerts": alerts,
        }

    def machine_snapshot(
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

        return {
            "machine_id": machine_id,
            "production": (
                production_service
                .summary(
                    machine_id
                )
            ),
            "oee": (
                oee_service.calculate(
                    machine_id,
                    planned_time_seconds=(
                        planned_time_seconds
                    ),
                    ideal_cycle_seconds=(
                        ideal_cycle_seconds
                    ),
                )
            ),
            "consumption": (
                consumption_service
                .summary(
                    machine_id
                )
            ),
            "telemetry": (
                telemetry_service
                .snapshot()
            ),
            "faults": (
                fault_service.list(
                    machine_id
                )
            ),
            "active_faults": (
                fault_service.list(
                    machine_id,
                    active_only=True,
                )
            ),
            "alerts": (
                alert_service.alerts(
                    machine_id
                )
            ),
            "active_alerts": (
                alert_service.alerts(
                    machine_id,
                    active_only=True,
                )
            ),
        }

    def health(
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

    def history(
        self,
        category: str,
        *,
        machine_id: str | None = None,
        limit: int | None = None,
    ):

        return (
            metrics_history_service.list(
                category,
                limit=limit,
                source=machine_id,
            )
        )


metrics_service = (
    MetricsService()
)
