from __future__ import annotations


from dataclasses import dataclass, field
from typing import Any




@dataclass
class Sensor:
    sensor_id: str
    name: str
    sensor_type: str
    device_id: str | None = None
    value: Any = None
    unit: str | None = None
    active: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)




class SensorManager:
    def __init__(self) -> None:
        self._sensors: dict[str, Sensor] = {}


    def register(
        self,
        sensor_id: str,
        name: str,
        sensor_type: str,
        device_id: str | None = None,
        unit: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Sensor:
        sensor = Sensor(
            sensor_id=sensor_id,
            name=name,
            sensor_type=sensor_type,
            device_id=device_id,
            unit=unit,
            metadata=metadata or {},
        )


        self._sensors[sensor_id] = sensor
        return sensor


    def get(self, sensor_id: str) -> Sensor | None:
        return self._sensors.get(sensor_id)


    def list(self) -> list[Sensor]:
        return list(self._sensors.values())


    def update(
        self,
        sensor_id: str,
        value: Any,
    ) -> Sensor:
        sensor = self.get(sensor_id)


        if sensor is None:
            raise KeyError(f"Sensor '{sensor_id}' not found")


        sensor.value = value
        return sensor


    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(sensor_id, None) is not None
