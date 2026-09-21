from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


def utc_now():
    return datetime.now(
        timezone.utc
    )


@dataclass
class MetricPoint:
    name: str
    value: float

    unit: str = ""

    source: str | None = None

    timestamp: datetime = field(
        default_factory=utc_now
    )

    tags: dict[str, str] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "unit": self.unit,
            "source": self.source,
            "timestamp": (
                self.timestamp
                .isoformat()
            ),
            "tags": dict(
                self.tags
            ),
            "metadata": dict(
                self.metadata
            ),
        }


@dataclass
class MachineCycle:
    machine_id: str

    duration_seconds: float

    good_units: int = 0
    rejected_units: int = 0

    started_at: datetime = field(
        default_factory=utc_now
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    @property
    def total_units(self):
        return (
            self.good_units
            + self.rejected_units
        )

    def to_dict(self):
        return {
            "machine_id": self.machine_id,
            "duration_seconds": (
                self.duration_seconds
            ),
            "good_units": (
                self.good_units
            ),
            "rejected_units": (
                self.rejected_units
            ),
            "total_units": (
                self.total_units
            ),
            "started_at": (
                self.started_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
        }


@dataclass
class DowntimeEvent:
    machine_id: str

    duration_seconds: float

    reason: str = ""

    category: str = "unplanned"

    timestamp: datetime = field(
        default_factory=utc_now
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "machine_id": self.machine_id,
            "duration_seconds": (
                self.duration_seconds
            ),
            "reason": self.reason,
            "category": self.category,
            "timestamp": (
                self.timestamp
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
  }
