"""
Servo motor simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
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

    def set_angle(
        self,
        angle,
    ):

        self.angle = max(
            0,
            min(
                180,
                int(angle),
            ),
        )

        runtime_pwm.write(
            self.pin,
            self.angle,
        )

    def get_angle(self):

        return self.angle

    def update(self):
        pass

    def reset(self):

        self.set_angle(0)
