from __future__ import annotations

from collections import defaultdict


class ConsumptionService:

    def __init__(self):
        self._totals = defaultdict(
            lambda: defaultdict(
                float
            )
        )

    def add(
        self,
        machine_id: str,
        resource: str,
        amount: float,
    ):

        normalized = str(
            resource
        ).strip()

        if not normalized:
            raise ValueError(
                "Resource is required"
            )

        value = float(
            amount
        )

        if value < 0:
            raise ValueError(
                "Consumption cannot "
                "be negative"
            )

        self._totals[
            machine_id
        ][
            normalized
        ] += value

        return self.get(
            machine_id,
            normalized,
        )

    def get(
        self,
        machine_id: str,
        resource: str,
    ):

        return float(
            self._totals[
                machine_id
            ].get(
                resource,
                0.0,
            )
        )

    def summary(
        self,
        machine_id: str,
    ):

        return {
            key: float(
                value
            )
            for (
                key,
                value,
            ) in self._totals[
                machine_id
            ].items()
        }

    def clear(self):
        self._totals.clear()


consumption_service = (
    ConsumptionService()
)
