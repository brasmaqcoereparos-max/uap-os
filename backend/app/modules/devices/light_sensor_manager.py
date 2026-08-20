from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LightSensor:
    sensor_id: str
    name: str
    device_id: str | None = None
    value: float = 0.0
    unit: str = "lux"
    minimum: float = 0.0
    maximum: float = 200000.0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(self, value: float) -> None:
        self.value = max(
            self.minimum,
            min(self.maximum, float(value)),
        )


class LightSensorManager:
    def __init__(self) -> None:
        self._sensors: dict[
            str,
            LightSensor,
        ] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        device_id: str | None = None,
        minimum: float = 0.0,
        maximum: float = 200000.0,
        unit: str = "lux",
        metadata: dict[str, Any] | None = None,
    ) -> LightSensor:
        sensor = LightSensor(
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
    ) -> LightSensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[LightSensor]:
        return list(self._sensors.values())

    def update(
        self,
        sensor_id: str,
        value: float,
    ) -> LightSensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Light sensor '{sensor_id}' not found"
            )

        sensor.update(value)
        return sensor

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
