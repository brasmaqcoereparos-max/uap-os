from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)

from app.modules.simulator.programming.simulator.runtime.runtime_pwm import (
    runtime_pwm,
)


class DCMotorDevice(DeviceBase):

    def __init__(
        self,
        name,
        pin,
    ):
        super().__init__(name)

        self.pin = pin

        self.speed = 0

    def update(self):

        self.speed = runtime_pwm.read(
            self.pin,
        )

    def stop(self):

        self.speed = 0

    def reset(self):

        self.stop()
