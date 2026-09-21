from __future__ import annotations

from app.modules.metrics.production_service import (
    production_service,
)


class OEEService:

    def calculate(
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

        total_units = int(
            summary[
                "total_units"
            ]
        )

        good_units = int(
            summary[
                "good_units"
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

        availability = (
            runtime / planned
            if planned > 0
            else 0.0
        )

        availability = min(
            1.0,
            max(
                0.0,
                availability,
            ),
        )

        if (
            ideal_cycle_seconds is not None
            and runtime > 0
            and total_units > 0
        ):
            performance = (
                float(
                    ideal_cycle_seconds
                )
                * total_units
                / runtime
            )

        else:
            performance = (
                1.0
                if total_units > 0
                else 0.0
            )

        performance = min(
            1.0,
            max(
                0.0,
                performance,
            ),
        )

        quality = (
            good_units
            / total_units
            if total_units > 0
            else 0.0
        )

        quality = min(
            1.0,
            max(
                0.0,
                quality,
            ),
        )

        oee = (
            availability
            * performance
            * quality
        )

        return {
            "machine_id": machine_id,
            "availability": (
                availability
            ),
            "performance": (
                performance
            ),
            "quality": quality,
            "oee": oee,
            "availability_percent": (
                round(
                    availability
                    * 100,
                    2,
                )
            ),
            "performance_percent": (
                round(
                    performance
                    * 100,
                    2,
                )
            ),
            "quality_percent": (
                round(
                    quality
                    * 100,
                    2,
                )
            ),
            "oee_percent": (
                round(
                    oee
                    * 100,
                    2,
                )
            ),
            "production": summary,
        }


oee_service = OEEService()
