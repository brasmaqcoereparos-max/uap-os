from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PowerSource:
    source_id: str
    name: str
    source_type: str = "battery"
    voltage: float = 0.0
    current: float = 0.0
    percentage: float = 0.0
    charging: bool = False
    online: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)

    def update(
        self,
        voltage: float,
        current: float,
        percentage: float | None = None,
        charging: bool | None = None,
    ) -> None:
        self.voltage = float(voltage)
        self.current = float(current)

        if percentage is not None:
            self.percentage = max(
                0.0,
                min(100.0, float(percentage)),
            )

        if charging is not None:
            self.charging = bool(charging)


class PowerManager:
    def __init__(self) -> None:
        self._sources: dict[str, PowerSource] = {}

    def register(
        self,
        source_id: str,
        name: str,
        source_type: str = "battery",
        metadata: dict[str, Any] | None = None,
    ) -> PowerSource:
        source = PowerSource(
            source_id=source_id,
            name=name,
            source_type=source_type,
            metadata=metadata or {},
        )

        self._sources[source_id] = source
        return source

    def get(self, source_id: str) -> PowerSource | None:
        return self._sources.get(source_id)

    def list(self) -> list[PowerSource]:
        return list(self._sources.values())

    def update(
        self,
        source_id: str,
        voltage: float,
        current: float,
        percentage: float | None = None,
        charging: bool | None = None,
    ) -> PowerSource:
        source = self.get(source_id)

        if source is None:
            raise KeyError(
                f"Power source '{source_id}' not found"
            )

        source.update(
            voltage,
            current,
            percentage,
            charging,
        )

        return source

    def remove(self, source_id: str) -> bool:
        return self._sources.pop(
            source_id,
            None,
        ) is not None
