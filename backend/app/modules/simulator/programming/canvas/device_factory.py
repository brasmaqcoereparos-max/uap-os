from app.modules.simulator.programming.canvas.device_base import (
    DeviceBase,
)


class DeviceFactory:

    def create(
        self,
        name,
    ):

        return DeviceBase(name)


device_factory = DeviceFactory()
