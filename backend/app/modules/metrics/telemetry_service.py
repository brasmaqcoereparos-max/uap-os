from __future__ import annotations

from collections import defaultdict

from app.modules.metrics.models import (
    MetricPoint,
)


class TelemetryService:

    def __init__(self):
        self._metrics: dict[
            str,
            list[MetricPoint],
        ] = defaultdict(
            list
        )

    def record(
        self,
        name: str,
        value: float,
        *,
        unit: str = "",
        source: str | None = None,
        tags=None,
        metadata=None,
    ):

        normalized = str(
            name
        ).strip()

        if not normalized:
            raise ValueError(
                "Metric name is required"
            )

        point = MetricPoint(
            name=normalized,
            value=float(
                value
            ),
            unit=str(
                unit
            ),
            source=source,
            tags=dict(
                tags or {}
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        self._metrics[
            normalized
        ].append(
            point
        )

        return point

    def latest(
        self,
        name: str,
    ):

        points = self._metrics.get(
            name,
            [],
        )

        if not points:
            return None

        return points[-1]

    def history(
        self,
        name: str,
        limit: int | None = None,
    ):

        points = list(
            self._metrics.get(
                name,
                [],
            )
        )

        if limit is not None:
            points = points[
                -max(
                    0,
                    int(limit),
                ):
            ]

        return points

    def snapshot(self):

        return {
            name: (
                points[-1].to_dict()
                if points
                else None
            )
            for (
                name,
                points,
            ) in self._metrics.items()
        }

    def clear(self):
        self._metrics.clear()


telemetry_service = (
    TelemetryService()
      )
