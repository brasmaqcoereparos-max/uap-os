from app.modules.simulator.programming.simulator.device.device_base import (
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

    def set_speed(self, speed):
        self.speed = max(
            0,
            min(100, int(speed)),
        )

        runtime_pwm.write(
            self.pin,
            self.speed,
        )

    def stop(self):
        self.set_speed(0)

    def update(self):
        pass

    def reset(self):
        self.stop()
