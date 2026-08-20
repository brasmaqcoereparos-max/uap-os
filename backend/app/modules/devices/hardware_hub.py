from __future__ import annotations

from app.modules.communication.device_discovery import (
    DeviceDiscovery,
)
from app.modules.communication.device_pairing import (
    DevicePairingManager,
)
from app.modules.communication.protocol_manager import (
    ProtocolManager,
)
from app.modules.devices.external_device_manager import (
    ExternalDeviceManager,
)
from app.modules.devices.hardware_gateway import (
    HardwareGateway,
)


class HardwareHub:
    """
    Centro universal de integração de hardware do UAP Box.
    """

    def __init__(self) -> None:
        self.discovery = DeviceDiscovery()
        self.pairing = DevicePairingManager()
        self.protocols = ProtocolManager()
        self.external_devices = (
            ExternalDeviceManager()
        )
        self.gateway = HardwareGateway()

    def register_device(
        self,
        device_id: str,
        name: str,
        controller_type: str,
        protocol: str,
        address: str | None = None,
        capabilities: list[str] | None = None,
    ):
        return self.external_devices.register(
            device_id=device_id,
            name=name,
            controller_type=controller_type,
            protocol=protocol,
            address=address,
            capabilities=capabilities,
        )

    def status(self) -> dict:
        return {
            "discovered_devices": len(
                self.discovery.list()
            ),
            "paired_sessions": len(
                self.pairing._sessions
            ),
            "protocols": len(
                self.protocols.list()
            ),
            "external_devices": len(
                self.external_devices.list()
            ),
            "gateway_devices": len(
                self.gateway.list()
            ),
        }
