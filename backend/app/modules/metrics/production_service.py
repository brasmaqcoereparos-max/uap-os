from __future__ import annotations

from app.modules.metrics.production_service import (
    production_service,
)


class ProductivityService:

    def calculate(
        self,
        machine_id: str,
        *,
        planned_time_seconds: (
            float | None
        ) = None,
    ):

        summary = (
            production_service
            .summary(
                machine_id
            )
        )

        runtime = float(
            summary[
                "runtime_seconds"
            ]
        )

        downtime = float(
            summary[
                "downtime_seconds"
            ]
        )

        if planned_time_seconds is None:
            planned = (
                runtime
                + downtime
            )

        else:
            planned = max(
                0.0,
                float(
                    planned_time_seconds
                ),
            )

        uptime = (
            runtime
            / planned
            if planned > 0
            else 0.0
        )

        downtime_ratio = (
            downtime
            / planned
            if planned > 0
            else 0.0
        )

        total_units = int(
            summary[
                "total_units"
            ]
        )

        productivity_per_hour = (
            total_units
            / (
                runtime
                / 3600.0
            )
            if runtime > 0
            else 0.0
        )

        return {
            "machine_id": (
                machine_id
            ),
            "planned_time_seconds": (
                planned
            ),
            "runtime_seconds": runtime,
            "downtime_seconds": downtime,
            "uptime_percent": round(
                min(
                    1.0,
                    max(
                        0.0,
                        uptime,
                    ),
                )
                * 100,
                2,
            ),
            "downtime_percent": round(
                min(
                    1.0,
                    max(
                        0.0,
                        downtime_ratio,
                    ),
                )
                * 100,
                2,
            ),
            "productivity_units_hour": (
                round(
                    productivity_per_hour,
                    4,
                )
            ),
            "total_units": (
                total_units
            ),
        }


productivity_service = (
    ProductivityService()
)
