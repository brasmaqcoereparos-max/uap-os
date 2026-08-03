
from app.modules.simulator.programming.simulator.devices.device_manager import (
    device_manager,
)


class DeviceRunner:

    def update(self):

        for device in device_manager.devices:

            if hasattr(device, "update"):

                device.update()


device_runner = DeviceRunner()
