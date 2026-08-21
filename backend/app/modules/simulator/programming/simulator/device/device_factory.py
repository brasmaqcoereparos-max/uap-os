"""
Fábrica central para criação de dispositivos UAP.
"""

from app.modules.simulator.programming.simulator.device.device_catalog import (
    device_catalog,
)


class DeviceFactory:

    def create(
        self,
        name,
        *args,
        **kwargs,
    ):

        device_class = device_catalog.get(
            name
        )

        if device_class is None:

            raise ValueError(
                f"Dispositivo '{name}' não registrado."
            )

        return device_class(
            *args,
            **kwargs,
        )

    def exists(
        self,
        name,
    ):

        return device_catalog.exists(
            name
        )

    def available_devices(self):

        return device_catalog.all()

    def count(self):

        return device_catalog.count()


device_factory = DeviceFactory()
