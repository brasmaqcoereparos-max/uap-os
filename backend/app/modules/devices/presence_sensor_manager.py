from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PresenceSensor:
    sensor_id: str
    name: str
    sensor_type: str = "pir"
    device_id: str | None = None
    detected: bool = False
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(self, detected: bool) -> None:
        self.detected = bool(detected)


class PresenceSensorManager:
    def __init__(self) -> None:
        self._sensors: dict[
            str,
            PresenceSensor,
        ] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        sensor_type: str = "pir",
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> PresenceSensor:
        sensor = PresenceSensor(
            sensor_id=sensor_id,
            name=name,
            sensor_type=sensor_type,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._sensors[sensor_id] = sensor
        return sensor

    def get(
        self,
        sensor_id: str,
    ) -> PresenceSensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[PresenceSensor]:
        return list(self._sensors.values())

    def update(
        self,
        sensor_id: str,
        detected: bool,
    ) -> PresenceSensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Presence sensor '{sensor_id}' not found"
            )

        sensor.update(detected)
        return sensor

    def any_detected(self) -> bool:
        return any(
            sensor.enabled and sensor.detected
            for sensor in self._sensors.values()
        )

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
