"""
Contexto central de hardware do UAP.

Une:
    HAL
    dispositivos
    capacidades
    mapeamentos
    comunicação
"""

from __future__ import annotations

from app.modules.communication.manager import (
    CommunicationManager,
)

from app.modules.devices.device_manager import (
    DeviceManager,
)

from app.modules.uhal.capability_registry import (
    create_default_registry,
)

from app.modules.uhal.hardware_abstraction import (
    HardwareAbstractionLayer,
)

from app.modules.uhal.logical_mapping import (
    LogicalMappingManager,
)


class UAPHardwareContext:

    def __init__(self) -> None:

        self.hal = (
            HardwareAbstractionLayer()
        )

        self.devices = (
            DeviceManager()
        )

        self.capabilities = (
            create_default_registry()
        )

        self.mappings = (
            LogicalMappingManager()
        )

        self.communication = (
            CommunicationManager()
        )

    def status(self) -> dict:

        return {
            "devices": (
                self.devices.count()
            ),
            "registered_capabilities": (
                self.capabilities.count()
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

    def get_capabilities(self):

        return self.capabilities.list()

    def has_capability(
        self,
        name,
    ):

        return self.capabilities.exists(
            name
        )

    def register_device(
        self,
        device,
    ):

        return self.devices.register(
            device
        )

    def get_device(
        self,
        device_id,
    ):

        return self.hal.get_device(
            device_id
        )

    def reset(self):

        for device in (
            self.hal.list_devices()
        ):

            self.hal.unregister_device(
                device.device_id
            )

        self.capabilities.clear()


uap_hardware_context = (
    UAPHardwareContext()
        )
