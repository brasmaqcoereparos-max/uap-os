"""
Descoberta de dispositivos do UAP.
"""

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

    def __init__(self):
        self.devices = {}

    def add(
        self,
        device: DiscoveredDevice,
    ):
        self.devices[device.device_id] = device
        return device

    def get(
        self,
        device_id: str,
    ):
        return self.devices.get(device_id)

    def remove(
        self,
        device_id: str,
    ):
        return self.devices.pop(
            device_id,
            None,
        )

    def list(self):
        return list(
            self.devices.values()
        )

    def clear(self):
        self.devices.clear()


__all__ = [
    "DiscoveredDevice",
    "DeviceDiscovery",
        ]
