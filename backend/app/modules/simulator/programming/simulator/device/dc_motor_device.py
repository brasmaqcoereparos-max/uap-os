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
        super().__init__(
            name=name,
            category="motion",
            description="Motor DC",
            icon="motor",
        )

        self.pin = pin

        self.speed = 0
        self.running = False

    def set_speed(self, speed):
        if not self.enabled:
            return False

        self.speed = max(
            0,
            min(
                100,
                int(speed),
            ),
        )

        self.running = (
            self.speed > 0
        )

        runtime_pwm.write(
            self.pin,
            self.speed,
        )

        return self.speed

    def start(self, speed=100):
        return self.set_speed(
            speed
        )

    def stop(self):
        self.speed = 0
        self.running = False

        runtime_pwm.write(
            self.pin,
            0,
        )

        return True

    def update(self):
        reader = getattr(
            runtime_pwm,
            "read",
            None,
        )

        if callable(reader):
            value = reader(
                self.pin
            )

            if value is not None:
                self.speed = max(
                    0,
                    min(
                        100,
                        int(value),
                    ),
                )

                self.running = (
                    self.speed > 0
                )

        return self.speed

    def reset(self):
        return self.stop()

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pin": self.pin,
            "speed": self.speed,
            "running": self.running,
        })

        return data
