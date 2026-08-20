from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SafetySensor:
    sensor_id: str
    name: str
    sensor_type: str
    active: bool = True
    triggered: bool = False
    device_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def trigger(self) -> None:
        self.triggered = True

    def reset(self) -> None:
        self.triggered = False


class SafetySensorManager:
    def __init__(self) -> None:
        self._sensors: dict[str, SafetySensor] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        sensor_type: str,
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> SafetySensor:
        sensor = SafetySensor(
            sensor_id=sensor_id,
            name=name,
            sensor_type=sensor_type,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._sensors[sensor_id] = sensor
        return sensor

    def get(self, sensor_id: str) -> SafetySensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[SafetySensor]:
        return list(self._sensors.values())

    def trigger(self, sensor_id: str) -> SafetySensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Safety sensor '{sensor_id}' not found"
            )

        sensor.trigger()
        return sensor

    def reset(self, sensor_id: str) -> SafetySensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Safety sensor '{sensor_id}' not found"
            )

        sensor.reset()
        return sensor

    def any_triggered(self) -> bool:
        return any(
            sensor.active and sensor.triggered
            for sensor in self._sensors.values()
        )

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
