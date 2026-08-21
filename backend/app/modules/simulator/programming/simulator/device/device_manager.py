"""
Gerenciador central das instâncias de dispositivos UAP.
"""

from app.modules.simulator.programming.simulator.device.device_registry import (
    device_registry,
)


class DeviceManager:

    def add(
        self,
        device,
    ):

        if device is None:
            raise ValueError(
                "O dispositivo não pode ser None."
            )

        return device_registry.register(
            device.name,
            device,
        )

    def get(
        self,
        name,
    ):

        return device_registry.get(
            name
        )

    def remove(
        self,
        name,
    ):

        return device_registry.unregister(
            name
        )

    def exists(
        self,
        name,
    ):

        return device_registry.exists(
            name
        )

    def all(self):

        return device_registry.all()

    def names(self):

        return device_registry.names()

    def count(self):

        return device_registry.count()

    def update_all(self):

        for device in (
            device_registry.all().values()
        ):

            if hasattr(
                device,
                "update",
            ):

                device.update()

    def reset_all(self):

        for device in (
            device_registry.all().values()
        ):

            if hasattr(
                device,
                "reset",
            ):

                device.reset()

    def clear(self):

        device_registry.clear()


device_manager = DeviceManager()
