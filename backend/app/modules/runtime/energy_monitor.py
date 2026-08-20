from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class EnergyReading:
    voltage: float
    current: float
    power: float
    timestamp: datetime


class EnergyMonitor:
    def __init__(self) -> None:
        self._readings: list[EnergyReading] = []

    def record(
        self,
        voltage: float,
        current: float,
    ) -> EnergyReading:
        voltage = float(voltage)
        current = float(current)

        reading = EnergyReading(
            voltage=voltage,
            current=current,
            power=voltage * current,
            timestamp=datetime.now(timezone.utc),
        )

        self._readings.append(reading)

        return reading

    def latest(self) -> EnergyReading | None:
        if not self._readings:
            return None

        return self._readings[-1]

    def readings(self) -> list[EnergyReading]:
        return list(self._readings)

    def average_power(self) -> float:
        if not self._readings:
            return 0.0

        return sum(
            reading.power
            for reading in self._readings
        ) / len(self._readings)

    def clear(self) -> None:
        self._readings.clear()
