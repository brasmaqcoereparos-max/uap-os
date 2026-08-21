
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


device_factory = DeviceFactory()
