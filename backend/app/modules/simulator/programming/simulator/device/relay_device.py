from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


class RelayDevice(DeviceBase):

    def __init__(

        self,

        name,

        pin,

    ):

        super().__init__(name)

        self.pin = pin

        self.state = False

    def update(self):

        self.state = runtime_gpio.read(

            self.pin,

        )

    def reset(self):

        self.state = False
