from __future__ import annotations

from app.modules.metrics.metrics_service import (
    metrics_service,
)
from app.modules.metrics.runtime_metrics_bridge import (
    runtime_metrics_bridge,
)


class RuntimeMetricsService:

    def attach(
        self,
        runtime_context,
    ):

        return (
            runtime_metrics_bridge
            .attach(
                runtime_context
            )
        )

    def detach(
        self,
        runtime_context,
    ):

        return (
            runtime_metrics_bridge
            .detach(
                runtime_context
            )
        )

    def snapshot(
        self,
        runtime_context,
        *,
        planned_time_seconds: (
            float | None
        ) = None,
        ideal_cycle_seconds: (
            float | None
        ) = None,
    ):

        machine_id = str(
            runtime_context.project_id
        )

        return {
            "runtime": (
                runtime_context
                .status()
            ),
            "metrics": (
                metrics_service
                .machine_snapshot(
                    machine_id,
                    planned_time_seconds=(
                        planned_time_seconds
                    ),
                    ideal_cycle_seconds=(
                        ideal_cycle_seconds
                    ),
                )
            ),
        }


runtime_metrics_service = (
    RuntimeMetricsService()
)
