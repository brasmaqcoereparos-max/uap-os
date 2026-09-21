from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field


class TelemetryCreate(BaseModel):
    name: str
    value: float

    machine_id: str | None = None

    unit: str = ""

    tags: dict[str, str] = Field(
        default_factory=dict
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class CycleCreate(BaseModel):
    machine_id: str

    duration_seconds: float

    good_units: int = 0
    rejected_units: int = 0

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class DowntimeCreate(BaseModel):
    machine_id: str

    duration_seconds: float

    reason: str = ""

    category: str = "unplanned"

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class ConsumptionCreate(BaseModel):
    machine_id: str

    resource: str

    amount: float

    unit: str = ""

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class FaultCreate(BaseModel):
    machine_id: str

    code: str

    message: str

    severity: str = "error"

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class AlertRuleCreate(BaseModel):
    id: str

    metric: str

    operator: str

    threshold: float

    level: str = "warning"

    message: str = ""

    machine_id: str | None = None

    enabled: bool = True


class MachineSnapshotRequest(BaseModel):
    planned_time_seconds: (
        float | None
    ) = None

    ideal_cycle_seconds: (
        float | None
    ) = None
