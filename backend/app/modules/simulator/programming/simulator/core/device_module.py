
"""
Módulo de dispositivos do Core UAP.
"""

from app.modules.simulator.programming.simulator.core.module import (
    Module,
)

from app.modules.simulator.programming.simulator.device.device_loader import (
    DeviceLoader,
)


class DeviceModule(Module):

    name = "Devices"
    version = "1.0"

    def __init__(self):
        super().__init__()

        self.loaded = False

    def register(self):
        if self.registered:
            return True

        result = DeviceLoader.load()

        self.loaded = True
        self.registered = True

        return (
            True
            if result is None
            else result
        )

    def boot(self):
        if self.booted:
            return True

        if not self.registered:
            self.register()

        self.booted = True

        return True

    def shutdown(self):
        self.booted = False

        return True

    def reset(self):
        self.booted = False
        self.registered = False
        self.loaded = False
        self.last_error = None

        return True
