from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExternalDevice:
    device_id: str
    name: str
    controller_type: str
    protocol: str
    address: str | None = None
    capabilities: list[str] = field(
        default_factory=list
    )
    connected: bool = False
    metadata: dict[str, Any] = field(
        default_factory=dict
    )


class ExternalDeviceManager:
    def __init__(self) -> None:
        self._devices: dict[
            str,
            ExternalDevice,
        ] = {}

    def register(
        self,
        device_id: str,
        name: str,
        controller_type: str,
        protocol: str,
        address: str | None = None,
        capabilities: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> ExternalDevice:
        device = ExternalDevice(
            device_id=device_id,
            name=name,
            controller_type=controller_type,
            protocol=protocol,
            address=address,
            capabilities=capabilities or [],
            metadata=metadata or {},
        )

        self._devices[device_id] = device

        return device

    def get(
        self,
        device_id: str,
    ) -> ExternalDevice | None:
        return self._devices.get(device_id)

    def list(self) -> list[ExternalDevice]:
        return list(self._devices.values())

    def set_connected(
        self,
        device_id: str,
        connected: bool,
    ) -> ExternalDevice:
        device = self.get(device_id)

        if device is None:
            raise KeyError(
                f"External device '{device_id}' not found"
            )

        device.connected = bool(connected)

        return device

    def remove(
        self,
        device_id: str,
    ) -> bool:
        return self._devices.pop(
            device_id,
            None,
        ) is not None
