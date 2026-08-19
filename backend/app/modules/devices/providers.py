from __future__ import annotations

from .network_provider import NetworkDiscoveryProvider
from .service import DeviceDiscoveryService


def create_default_discovery_service() -> DeviceDiscoveryService:
    service = DeviceDiscoveryService()

    service.register_provider(
        "network",
        NetworkDiscoveryProvider(),
    )

    return service
