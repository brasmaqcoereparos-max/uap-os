from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TemperatureSensor:
    sensor_id: str
    name: str
    device_id: str | None = None
    temperature: float = 25.0
    unit: str = "C"
    minimum: float = -100.0
    maximum: float = 200.0
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(self, temperature: float) -> None:
        value = float(temperature)

        self.temperature = max(
            self.minimum,
            min(self.maximum, value),
        )


class TemperatureManager:
    def __init__(self) -> None:
        self._sensors: dict[
            str,
            TemperatureSensor,
        ] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        device_id: str | None = None,
        minimum: float = -100.0,
        maximum: float = 200.0,
        unit: str = "C",
        metadata: dict[str, Any] | None = None,
    ) -> TemperatureSensor:
        sensor = TemperatureSensor(
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
    ) -> TemperatureSensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[TemperatureSensor]:
        return list(self._sensors.values())

    def update(
        self,
        sensor_id: str,
        temperature: float,
    ) -> TemperatureSensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Temperature sensor '{sensor_id}' not found"
            )

        sensor.update(temperature)
        return sensor

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
