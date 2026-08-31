from __future__ import annotations

from app.modules.devices.network_provider import (
    NetworkDiscoveryProvider,
)

from app.modules.devices.discovery.service import (
    DeviceDiscoveryService,
)


def create_default_discovery_service(
) -> DeviceDiscoveryService:
    service = (
        DeviceDiscoveryService()
    )

    service.register_provider(
        "network",
        NetworkDiscoveryProvider(),
    )

    return service
