from __future__ import annotations

from app.modules.metrics.aggregation_service import (
    metrics_aggregation_service,
)
from app.modules.metrics.alert_service import (
    alert_service,
)
from app.modules.metrics.consumption_service import (
    consumption_service,
)
from app.modules.metrics.dashboard_service import (
    metrics_dashboard_service,
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
from app.modules.metrics.persistence import (
    metrics_persistence,
)
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.productivity_service import (
    productivity_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)


class MetricsService:

    STORE_NAME = (
        "metrics_history"
    )

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

    def record_cycle(
        self,
        machine_id: str,
        duration_seconds: float,
        *,
        good_units: int = 0,
        rejected_units: int = 0,
        metadata=None,
    ):

        cycle = (
            production_service
            .record_cycle(
                machine_id,
                duration_seconds,
                good_units=(
                    good_units
                ),
                rejected_units=(
                    rejected_units
                ),
                metadata=metadata,
            )
        )

        metrics_history_service.record(
            "cycle",
            cycle.to_dict(),
            source=machine_id,
        )

        return cycle.to_dict()

    def record_downtime(
        self,
        machine_id: str,
        duration_seconds: float,
        *,
        reason: str = "",
        category: str = "unplanned",
        metadata=None,
    ):

        event = (
            production_service
            .record_downtime(
                machine_id,
                duration_seconds,
                reason=reason,
                category=category,
                metadata=metadata,
            )
        )

        metrics_history_service.record(
            "downtime",
            event.to_dict(),
            source=machine_id,
        )

        return event.to_dict()

    def record_consumption(
        self,
        machine_id: str,
        resource: str,
        amount: float,
        *,
        unit: str = "",
        metadata=None,
    ):

        total = (
            consumption_service.add(
                machine_id,
                resource,
                amount,
            )
        )

        result = {
            "machine_id": (
                machine_id
            ),
            "resource": resource,
            "amount": float(
                amount
            ),
            "total": total,
            "unit": unit,
            "metadata": dict(
                metadata or {}
            ),
        }

        metrics_history_service.record(
            "consumption",
            result,
            source=machine_id,
        )

        return result

    def record_fault(
        self,
        machine_id: str,
        code: str,
        message: str,
        *,
        severity: str = "error",
        metadata=None,
    ):

        return fault_service.record(
            machine_id=machine_id,
            code=code,
            message=message,
            severity=severity,
            metadata=metadata,
        )

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
            "machine_id": (
                machine_id
            ),
            "production": (
                production_service
                .summary(
                    machine_id
                )
            ),
            "productivity": (
                productivity_service
                .calculate(
                    machine_id,
                    planned_time_seconds=(
                        planned_time_seconds
                    ),
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

    def dashboard(
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
            metrics_dashboard_service
            .machine(
                machine_id,
                planned_time_seconds=(
                    planned_time_seconds
                ),
                ideal_cycle_seconds=(
                    ideal_cycle_seconds
                ),
            )
        )

    def aggregate(
        self,
        metric_name: str,
        *,
        machine_id: str | None = None,
        start=None,
        end=None,
    ):

        return (
            metrics_aggregation_service
            .aggregate_telemetry(
                metric_name,
                machine_id=(
                    machine_id
                ),
                start=start,
                end=end,
            )
        )

    def history(
        self,
        category: str,
        *,
        machine_id: str | None = None,
        limit: int | None = None,
        start=None,
        end=None,
    ):

        return (
            metrics_history_service
            .list(
                category,
                source=machine_id,
                limit=limit,
                start=start,
                end=end,
            )
        )

    def save_history(self):

        path = (
            metrics_persistence.save(
                self.STORE_NAME,
                {
                    "history": (
                        metrics_history_service
                        .export_all()
                    ),
                },
            )
        )

        return {
            "saved": True,
            "path": str(
                path
            ),
        }

    def load_history(self):

        data = (
            metrics_persistence.load(
                self.STORE_NAME
            )
        )

        if data is None:
            return {
                "loaded": False,
            }

        metrics_history_service.import_all(
            data.get(
                "history",
                {},
            ),
            replace=True,
        )

        return {
            "loaded": True,
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


metrics_service = (
    MetricsService()
        )
