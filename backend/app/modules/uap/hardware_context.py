from __future__ import annotations

from app.modules.communication.manager import CommunicationManager
from app.modules.devices.device_manager import DeviceManager
from app.modules.uhal.capability_registry import create_default_registry
from app.modules.uhal.hardware_abstraction import HardwareAbstractionLayer
from app.modules.uhal.logical_mapping import LogicalMappingManager


class UAPHardwareContext:
    """
    Ponto central da infraestrutura de hardware do UAP.

    Mantém os principais serviços desacoplados,
    permitindo que o Studio, Runtime e IA utilizem
    a mesma infraestrutura.
    """

    def __init__(self) -> None:
        self.hal = HardwareAbstractionLayer()
        self.devices = DeviceManager()
        self.capabilities = create_default_registry()
        self.mappings = LogicalMappingManager()
        self.communication = CommunicationManager()

    def status(self) -> dict:
        return {
            "devices": self.devices.count(),
            "registered_capabilities": len(
                self.capabilities.list()
            ),
            "logical_mappings": len(
                self.mappings.list()
            ),
            "communication_channels": len(
                self.communication.list()
            ),
            "hardware_devices": len(
                self.hal.list_devices()
            ),
        }
