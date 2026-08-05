from app.modules.automation.device_registry import (
    device_registry,
)


class DeviceManager:

    def initialize_all(self):

        for device in device_registry.all():

            device.initialize()

    def update_all(self):

        for device in device_registry.all():

            if device.enabled:

                device.update()

    def shutdown_all(self):

        for device in device_registry.all():

            device.shutdown()


device_manager = DeviceManager()
