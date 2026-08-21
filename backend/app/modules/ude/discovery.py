"""
Descoberta de dispositivos do Universal Device Engine.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DiscoveryResult:
    device_id: str
    name: str
    device_type: str
    protocol: str | None = None
    address: str | None = None
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class DeviceDiscovery:

    def __init__(self):
        self.devices = {}

    def add(
        self,
        device_id,
        name,
        device_type,
        protocol=None,
        address=None,
        metadata=None,
    ):
        result = DiscoveryResult(
            device_id=device_id,
            name=name,
            device_type=device_type,
            protocol=protocol,
            address=address,
            metadata=metadata or {},
        )

        self.devices[device_id] = result

        return result

    def get(
        self,
        device_id,
    ):
        return self.devices.get(
            device_id
        )

    def remove(
        self,
        device_id,
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
