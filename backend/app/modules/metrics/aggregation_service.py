from __future__ import annotations

from collections import defaultdict
from datetime import datetime

from app.modules.metrics.history_service import (
    metrics_history_service,
)


class MetricsAggregationService:

    def aggregate_telemetry(
        self,
        metric_name: str,
        *,
        machine_id: str | None = None,
        start: (
            datetime | str | None
        ) = None,
        end: (
            datetime | str | None
        ) = None,
    ):

        items = (
            metrics_history_service
            .list(
                "telemetry",
                source=machine_id,
                start=start,
                end=end,
            )
        )

        values = []

        for item in items:

            data = item.get(
                "data",
                {},
            )

            if (
                data.get(
                    "name"
                )
                != metric_name
            ):
                continue

            value = data.get(
                "value"
            )

            if value is None:
                continue

            values.append(
                float(
                    value
                )
            )

        if not values:
            return {
                "metric": metric_name,
                "count": 0,
                "min": None,
                "max": None,
                "average": None,
                "sum": 0.0,
            }

        return {
            "metric": metric_name,
            "count": len(
                values
            ),
            "min": min(
                values
            ),
            "max": max(
                values
            ),
            "average": (
                sum(
                    values
                )
                / len(
                    values
                )
            ),
            "sum": sum(
                values
            ),
        }

    def group_count_by_day(
        self,
        category: str,
        *,
        machine_id: str | None = None,
    ):

        items = (
            metrics_history_service
            .list(
                category,
                source=machine_id,
            )
        )

        groups = defaultdict(
            int
        )

        for item in items:
            timestamp = (
                datetime.fromisoformat(
                    item[
                        "timestamp"
                    ]
                )
            )

            key = timestamp.date().isoformat()

            groups[
                key
            ] += 1

        return dict(
            sorted(
                groups.items()
            )
        )


metrics_aggregation_service = (
    MetricsAggregationService()
                  )
