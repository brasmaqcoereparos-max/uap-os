from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Pump:
    pump_id: str
    name: str
    device_id: str | None = None
    power: float = 0.0
    running: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)

    def start(self, power: float = 100.0) -> None:
        self.power = max(
            0.0,
            min(100.0, float(power)),
        )
        self.running = True

    def stop(self) -> None:
        self.running = False
        self.power = 0.0


class PumpManager:
    def __init__(self) -> None:
        self._pumps: dict[str, Pump] = {}

    def register(
        self,
        pump_id: str,
        name: str,
        device_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Pump:
        pump = Pump(
            pump_id=pump_id,
            name=name,
            device_id=device_id,
            metadata=metadata or {},
        )

        self._pumps[pump_id] = pump
        return pump

    def get(self, pump_id: str) -> Pump | None:
        return self._pumps.get(pump_id)

    def list(self) -> list[Pump]:
        return list(self._pumps.values())

    def start(
        self,
        pump_id: str,
        power: float = 100.0,
    ) -> Pump:
        pump = self.get(pump_id)

        if pump is None:
            raise KeyError(f"Pump '{pump_id}' not found")

        pump.start(power)
        return pump

    def stop(self, pump_id: str) -> Pump:
        pump = self.get(pump_id)

        if pump is None:
            raise KeyError(f"Pump '{pump_id}' not found")

        pump.stop()
        return pump

    def remove(self, pump_id: str) -> bool:
        return self._pumps.pop(
            pump_id,
            None,
        ) is not None
