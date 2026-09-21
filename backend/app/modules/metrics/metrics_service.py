from __future__ import annotations

from app.modules.metrics.consumption_service import (
    consumption_service,
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
        }


metrics_service = (
    MetricsService()
)
