from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


class ButtonDevice(DeviceBase):

    def __init__(

        self,

        name,

        pin,

    ):

        super().__init__(name)

        self.pin = pin

    def press(self):

        runtime_gpio.write(

            self.pin,

            True,

        )

    def release(self):

        runtime_gpio.write(

            self.pin,

            False,

        )

    def update(self):

        pass

    def reset(self):

        self.release()
