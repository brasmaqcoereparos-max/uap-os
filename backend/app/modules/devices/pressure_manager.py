from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PressureSensor:
    sensor_id: str
    name: str
    device_id: str | None = None
    pressure: float = 0.0
    unit: str = "bar"
    minimum: float = 0.0
    maximum: float = 1000.0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(self, pressure: float) -> None:
        value = float(pressure)

        self.pressure = max(
            self.minimum,
            min(self.maximum, value),
        )


class PressureManager:
    def __init__(self) -> None:
        self._sensors: dict[
            str,
            PressureSensor,
        ] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        device_id: str | None = None,
        minimum: float = 0.0,
        maximum: float = 1000.0,
        unit: str = "bar",
        metadata: dict[str, Any] | None = None,
    ) -> PressureSensor:
        sensor = PressureSensor(
            sensor_id=sensor_id,
            name=name,
            device_id=device_id,
            minimum=minimum,
            maximum=maximum,
            unit=unit,
            metadata=metadata or {},
        )

        self._sensors[sensor_id] = sensor
        return sensor

    def get(
        self,
        sensor_id: str,
    ) -> PressureSensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[PressureSensor]:
        return list(self._sensors.values())

    def update(
        self,
        sensor_id: str,
        pressure: float,
    ) -> PressureSensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Pressure sensor '{sensor_id}' not found"
            )

        sensor.update(pressure)
        return sensor

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
