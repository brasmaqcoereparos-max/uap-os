from __future__ import annotations

from collections import defaultdict

from app.modules.metrics.models import (
    DowntimeEvent,
    MachineCycle,
)


class ProductionService:

    def __init__(self):
        self._cycles: dict[
            str,
            list[MachineCycle],
        ] = defaultdict(
            list
        )

        self._downtime: dict[
            str,
            list[DowntimeEvent],
        ] = defaultdict(
            list
        )

    def record_cycle(
        self,
        machine_id: str,
        duration_seconds: float,
        *,
        good_units: int = 0,
        rejected_units: int = 0,
        metadata=None,
    ):

        if duration_seconds < 0:
            raise ValueError(
                "Cycle duration cannot "
                "be negative"
            )

        cycle = MachineCycle(
            machine_id=machine_id,
            duration_seconds=float(
                duration_seconds
            ),
            good_units=max(
                0,
                int(
                    good_units
                ),
            ),
            rejected_units=max(
                0,
                int(
                    rejected_units
                ),
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        self._cycles[
            machine_id
        ].append(
            cycle
        )

        return cycle

    def record_downtime(
        self,
        machine_id: str,
        duration_seconds: float,
        *,
        reason: str = "",
        category: str = "unplanned",
        metadata=None,
    ):

        if duration_seconds < 0:
            raise ValueError(
                "Downtime duration cannot "
                "be negative"
            )

        event = DowntimeEvent(
            machine_id=machine_id,
            duration_seconds=float(
                duration_seconds
            ),
            reason=reason,
            category=category,
            metadata=dict(
                metadata or {}
            ),
        )

        self._downtime[
            machine_id
        ].append(
            event
        )

        return event

    def cycles(
        self,
        machine_id: str,
    ):
        return list(
            self._cycles.get(
                machine_id,
                [],
            )
        )

    def downtime(
        self,
        machine_id: str,
    ):
        return list(
            self._downtime.get(
                machine_id,
                [],
            )
        )

    def summary(
        self,
        machine_id: str,
    ):

        cycles = self.cycles(
            machine_id
        )

        downtime = self.downtime(
            machine_id
        )

        good_units = sum(
            cycle.good_units
            for cycle in cycles
        )

        rejected_units = sum(
            cycle.rejected_units
            for cycle in cycles
        )

        runtime_seconds = sum(
            cycle.duration_seconds
            for cycle in cycles
        )

        downtime_seconds = sum(
            event.duration_seconds
            for event in downtime
        )

        return {
            "machine_id": machine_id,
            "cycles": len(
                cycles
            ),
            "good_units": good_units,
            "rejected_units": (
                rejected_units
            ),
            "total_units": (
                good_units
                + rejected_units
            ),
            "runtime_seconds": (
                runtime_seconds
            ),
            "downtime_seconds": (
                downtime_seconds
            ),
        }

    def clear(self):
        self._cycles.clear()
        self._downtime.clear()


production_service = (
    ProductionService()
      )
