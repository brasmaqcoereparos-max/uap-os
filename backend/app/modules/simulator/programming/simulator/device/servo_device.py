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
        super().__init__(
            name=name,
            category="motion",
            description="Servo motor",
            icon="servo",
        )

        self.pin = pin
        self.angle = 0

        self.minimum_angle = 0
        self.maximum_angle = 180

    def set_angle(self, angle):
        if not self.enabled:
            return False

        angle = int(angle)

        self.angle = max(
            self.minimum_angle,
            min(
                self.maximum_angle,
                angle,
            ),
        )

        runtime_pwm.write(
            self.pin,
            self.angle,
        )

        return self.angle

    def get_angle(self):
        return self.angle

    def set_limits(
        self,
        minimum,
        maximum,
    ):
        minimum = int(minimum)
        maximum = int(maximum)

        if minimum >= maximum:
            raise ValueError(
                "Limites do servo "
                "são inválidos."
            )

        self.minimum_angle = (
            minimum
        )

        self.maximum_angle = (
            maximum
        )

        self.angle = max(
            minimum,
            min(
                maximum,
                self.angle,
            ),
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
                self.angle = int(
                    value
                )

        return self.angle

    def reset(self):
        return self.set_angle(
            self.minimum_angle
        )

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pin": self.pin,
            "angle": self.angle,
            "minimum_angle": (
                self.minimum_angle
            ),
            "maximum_angle": (
                self.maximum_angle
            ),
        })

        return data
