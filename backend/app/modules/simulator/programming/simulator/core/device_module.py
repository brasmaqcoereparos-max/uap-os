from app.modules.simulator.programming.simulator.core.module import (
    Module,
)

from app.modules.simulator.programming.simulator.device.device_loader import (
    DeviceLoader,
)


class DeviceModule(Module):

    name = "Devices"

    version = "1.0"

    def register(self):

        DeviceLoader.load()

    def boot(self):

        pass
