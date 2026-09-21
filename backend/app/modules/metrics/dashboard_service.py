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
from app.modules.metrics.oee_service import (
    oee_service,
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


class MetricsDashboardService:

    def machine(
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

        production = (
            production_service.summary(
                machine_id
            )
        )

        productivity = (
            productivity_service
            .calculate(
                machine_id,
                planned_time_seconds=(
                    planned_time_seconds
                ),
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

        faults = fault_service.list(
            machine_id,
            active_only=True,
        )

        alerts = alert_service.alerts(
            machine_id,
            active_only=True,
        )

        return {
            "machine_id": machine_id,
            "summary": {
                "cycles": (
                    production[
                        "cycles"
                    ]
                ),
                "total_units": (
                    production[
                        "total_units"
                    ]
                ),
                "good_units": (
                    production[
                        "good_units"
                    ]
                ),
                "rejected_units": (
                    production[
                        "rejected_units"
                    ]
                ),
                "uptime_percent": (
                    productivity[
                        "uptime_percent"
                    ]
                ),
                "downtime_percent": (
                    productivity[
                        "downtime_percent"
                    ]
                ),
                "oee_percent": (
                    oee[
                        "oee_percent"
                    ]
                ),
                "active_faults": len(
                    faults
                ),
                "active_alerts": len(
                    alerts
                ),
            },
            "production": production,
            "productivity": productivity,
            "oee": oee,
            "consumption": (
                consumption_service
                .summary(
                    machine_id
                )
            ),
            "faults": faults,
            "alerts": alerts,
            "telemetry": (
                telemetry_service
                .snapshot()
            ),
        }

    def fleet(
        self,
        machine_ids: list[str],
    ):

        machines = [
            self.machine(
                machine_id
            )
            for machine_id
            in machine_ids
        ]

        total_units = sum(
            machine[
                "summary"
            ][
                "total_units"
            ]
            for machine
            in machines
        )

        active_faults = sum(
            machine[
                "summary"
            ][
                "active_faults"
            ]
            for machine
            in machines
        )

        active_alerts = sum(
            machine[
                "summary"
            ][
                "active_alerts"
            ]
            for machine
            in machines
        )

        oee_values = [
            machine[
                "summary"
            ][
                "oee_percent"
            ]
            for machine
            in machines
        ]

        average_oee = (
            sum(
                oee_values
            )
            / len(
                oee_values
            )
            if oee_values
            else 0.0
        )

        return {
            "machines": machines,
            "summary": {
                "machine_count": len(
                    machines
                ),
                "total_units": (
                    total_units
                ),
                "active_faults": (
                    active_faults
                ),
                "active_alerts": (
                    active_alerts
                ),
                "average_oee_percent": (
                    round(
                        average_oee,
                        2,
                    )
                ),
            },
        }


metrics_dashboard_service = (
    MetricsDashboardService()
      )
