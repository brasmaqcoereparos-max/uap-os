from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_pwm import (
    runtime_pwm,
)


class BuzzerDevice(DeviceBase):

    def __init__(

        self,

        name,

        pin,

    ):

        super().__init__(name)

        self.pin = pin

        self.level = 0

    def update(self):

        self.level = runtime_pwm.read(

            self.pin,

        )

    def reset(self):

        self.level = 0
