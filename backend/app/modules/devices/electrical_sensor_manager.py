from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ElectricalReading:
    voltage: float = 0.0
    current: float = 0.0

    @property
    def power(self) -> float:
        return self.voltage * self.current


@dataclass
class ElectricalSensor:
    sensor_id: str
    name: str
    device_id: str | None = None
    reading: ElectricalReading = field(
        default_factory=ElectricalReading
    )
    enabled: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(
        self,
        voltage: float,
        current: float,
    ) -> None:
        self.reading = ElectricalReading(
            voltage=float(voltage),
            current=float(current),
        )


class ElectricalSensorManager:
    def __init__(self) -> None:
        self._sensors: dict[
            str,
            ElectricalSensor,
        ] = {}

    def register(
        self,
        sensor_id: str,
        name: str,
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> ElectricalSensor:
        sensor = ElectricalSensor(
            sensor_id=sensor_id,
            name=name,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._sensors[sensor_id] = sensor
        return sensor

    def get(
        self,
        sensor_id: str,
    ) -> ElectricalSensor | None:
        return self._sensors.get(sensor_id)

    def list(self) -> list[ElectricalSensor]:
        return list(self._sensors.values())

    def update(
        self,
        sensor_id: str,
        voltage: float,
        current: float,
    ) -> ElectricalSensor:
        sensor = self.get(sensor_id)

        if sensor is None:
            raise KeyError(
                f"Electrical sensor '{sensor_id}' not found"
            )

        sensor.update(voltage, current)
        return sensor

    def remove(self, sensor_id: str) -> bool:
        return self._sensors.pop(
            sensor_id,
            None,
        ) is not None
