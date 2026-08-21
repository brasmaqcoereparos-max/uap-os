"""
LED simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


class LEDDevice(DeviceBase):

    def __init__(
        self,
        name,
        pin,
    ):
        super().__init__(name)

        self.pin = pin
        self.state = False

    def on(self):

        self.state = True

        runtime_gpio.write(
            self.pin,
            True,
        )

    def off(self):

        self.state = False

        runtime_gpio.write(
            self.pin,
            False,
        )

    def toggle(self):

        if self.state:
            self.off()
        else:
            self.on()

    def update(self):
        pass

    def reset(self):

        self.off()
