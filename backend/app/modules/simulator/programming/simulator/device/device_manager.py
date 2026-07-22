from app.modules.simulator.programming.simulator.devices.device_registry import (
    device_registry,
)


class DeviceManager:

    def add(

        self,

        device,

    ):

        device_registry.register(

            device.name,

            device,

        )

    def update_all(self):

        for device in device_registry.all().values():

            device.update()

    def reset_all(self):

        for device in device_registry.all().values():

            device.reset()


device_manager = DeviceManager()
