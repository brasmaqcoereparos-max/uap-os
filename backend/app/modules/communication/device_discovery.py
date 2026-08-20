from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DiscoveredDevice:
    device_id: str
    name: str
    protocol: str
    address: str | None = None
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class DeviceDiscovery:
    def __init__(self) -> None:
        self._devices: dict[
            str,
            DiscoveredDevice,
        ] = {}

    def add(
        self,
        device_id: str,
        name: str,
        protocol: str,
        address: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> DiscoveredDevice:
        device = DiscoveredDevice(
            device_id=device_id,
            name=name,
            protocol=protocol,
            address=address,
            metadata=metadata or {},
        )

        self._devices[device_id] = device
        return device

    def get(
        self,
        device_id: str,
    ) -> DiscoveredDevice | None:
        return self._devices.get(device_id)

    def list(self) -> list[DiscoveredDevice]:
        return list(self._devices.values())

    def by_protocol(
        self,
        protocol: str,
    ) -> list[DiscoveredDevice]:
        return [
            device
            for device in self._devices.values()
            if device.protocol == protocol
        ]

    def remove(
        self,
        device_id: str,
    ) -> bool:
        return self._devices.pop(
            device_id,
            None,
        ) is not None

    def clear(self) -> None:
        self._devices.clear()
