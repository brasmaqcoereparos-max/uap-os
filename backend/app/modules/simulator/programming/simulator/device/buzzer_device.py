from app.modules.simulator.programming.simulator.device.device_base import (
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
        super().__init__(
            name=name,
            category="output",
            description="Buzzer PWM",
            icon="volume",
        )

        self.pin = pin
        self.level = 0

    def set_level(self, level):
        if not self.enabled:
            return False

        self.level = max(
            0,
            min(
                100,
                int(level),
            ),
        )

        runtime_pwm.write(
            self.pin,
            self.level,
        )

        return self.level

    def on(self, level=100):
        return self.set_level(level)

    def off(self):
        self.level = 0

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
                self.level = int(value)

        return self.level

    def reset(self):
        return self.off()

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pin": self.pin,
            "level": self.level,
        })

        return data
