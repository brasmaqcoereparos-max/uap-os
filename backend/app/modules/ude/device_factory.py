from app.modules.ude.device import Device
from app.modules.ude.device_registry import device_registry


class DeviceFactory:

    def create(
        self,
        device_type,
        name,
    ):

        device = device_registry.create(
            device_type,
            name,
            device_type,
        )

        if device is not None:
            return device

        return Device(
            name,
            device_type,
        )


device_factory = DeviceFactory()"""
Universal Device Engine
"""
