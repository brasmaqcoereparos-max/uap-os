from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Calibration:
    device_id: str
    offsets: dict[str, float] = field(
        default_factory=dict
    )
    scales: dict[str, float] = field(
        default_factory=dict
    )
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def apply(
        self,
        channel: str,
        value: float,
    ) -> float:
        offset = self.offsets.get(channel, 0.0)
        scale = self.scales.get(channel, 1.0)

        return (
            (float(value) + offset)
            * scale
        )


class CalibrationManager:
    def __init__(self) -> None:
        self._calibrations: dict[
            str,
            Calibration,
        ] = {}

    def create(
        self,
        device_id: str,
        offsets: dict[str, float] | None = None,
        scales: dict[str, float] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Calibration:
        calibration = Calibration(
            device_id=device_id,
            offsets=offsets or {},
            scales=scales or {},
            metadata=metadata or {},
        )

        self._calibrations[device_id] = calibration

        return calibration

    def get(
        self,
        device_id: str,
    ) -> Calibration | None:
        return self._calibrations.get(device_id)

    def set_offset(
        self,
        device_id: str,
        channel: str,
        value: float,
    ) -> Calibration:
        calibration = self.get(device_id)

        if calibration is None:
            calibration = self.create(device_id)

        calibration.offsets[channel] = float(value)

        return calibration

    def set_scale(
        self,
        device_id: str,
        channel: str,
        value: float,
    ) -> Calibration:
        calibration = self.get(device_id)

        if calibration is None:
            calibration = self.create(device_id)

        calibration.scales[channel] = float(value)

        return calibration

    def remove(
        self,
        device_id: str,
    ) -> bool:
        return (
            self._calibrations.pop(
                device_id,
                None,
            )
            is not None
        )
