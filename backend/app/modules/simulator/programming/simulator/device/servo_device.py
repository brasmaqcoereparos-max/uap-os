from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_pwm import (
    runtime_pwm,
)


class ServoDevice(DeviceBase):

    def __init__(

        self,

        name,

        pin,

    ):

        super().__init__(name)

        self.pin = pin

        self.angle = 0

    def update(self):

        pwm = runtime_pwm.read(

            self.pin,

        )

        self.angle = int(

            pwm * 180 / 255,

        )

    def reset(self):

        self.angle = 0
