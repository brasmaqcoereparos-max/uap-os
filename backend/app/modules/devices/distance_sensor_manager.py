from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DistanceSensor:
    sensor_id: str
    name: str
    sensor_type: str = "ultrasonic"
    device_id: str | None = None
    distance: float = 0.0
    unit: str = "mm"
    minimum: float = 0.0
    maximum: float = 10000.0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(self, distance: float) -> None:
        value = float(distance)

        self.distance = max(
            self.minimum,
            min(self.maximum, value),
        )

    def in_range(self) -> bool:
        return (
            self.minimum
            <= self.distance
            <= self.maximum
        )


class DistanceSensorManager:
    def __init__(self) -> None:
        self._sensors: dict[str, DistanceSensor] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        sensor_type: str = "ultrasonic",
        device_id: str | None = None,
        minimum: float = 0.0,
        maximum: float = 10000.0,
        unit: str = "mm",
        metadata: dict[str, Any] | None = None,
    ) -> DistanceSensor:
        sensor = DistanceSensor(
            sensor_id=sensor_id,
            name=name,
            sensor_type=sensor_type,
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
    ) -> DistanceSensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[DistanceSensor]:
        return list(self._sensors.values())

    def update(
        self,
        sensor_id: str,
        distance: float,
    ) -> DistanceSensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Distance sensor '{sensor_id}' not found"
            )

        sensor.update(distance)
        return sensor

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
