from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass
class UIDataPoint:
    value: float

    label: str | None = None
    timestamp: datetime | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "value": self.value,
            "label": self.label,
            "timestamp": (
                self.timestamp.isoformat()
                if self.timestamp
                else None
            ),
            "metadata": dict(
                self.metadata
            ),
        }


@dataclass
class UIDataSeries:
    id: str
    name: str

    points: list[
        UIDataPoint
    ] = field(
        default_factory=list
    )

    max_points: int = 1000

    def add(
        self,
        point: UIDataPoint,
    ):
        self.points.append(point)

        if (
            self.max_points > 0
            and len(self.points)
            > self.max_points
        ):
            excess = (
                len(self.points)
                - self.max_points
            )

            del self.points[:excess]

        return point

    def clear(self):
        self.points.clear()

    def latest(self):
        if not self.points:
            return None

        return self.points[-1]

    def values(self):
        return [
            point.value
            for point in self.points
        ]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "max_points": (
                self.max_points
            ),
            "points": [
                point.to_dict()
                for point in self.points
            ],
}
