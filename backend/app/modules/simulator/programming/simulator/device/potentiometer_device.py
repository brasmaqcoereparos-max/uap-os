from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class PotentiometerDevice(DeviceBase):

    def __init__(
        self,
        name,
        pin,
        minimum=0,
        maximum=1023,
    ):
        super().__init__(
            name=name,
            category="input",
            description="Potenciômetro analógico",
            icon="sliders",
        )

        self.pin = pin

        self.minimum = int(minimum)
        self.maximum = int(maximum)

        if self.minimum >= self.maximum:
            raise ValueError(
                "Faixa do potenciômetro inválida."
            )

        self.value = self.minimum

    def set_value(self, value):
        if not self.enabled:
            return False

        self.value = max(
            self.minimum,
            min(
                self.maximum,
                int(value),
            ),
        )

        return self.value

    def read(self):
        return self.value

    def normalized(self):
        span = (
            self.maximum
            - self.minimum
        )

        if span <= 0:
            return 0.0

        return (
            self.value
            - self.minimum
        ) / span

    def percentage(self):
        return round(
            self.normalized() * 100,
            2,
        )

    def update(self):
        return self.value

    def reset(self):
        self.value = self.minimum
        return self.value

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pin": self.pin,
            "value": self.value,
            "minimum": self.minimum,
            "maximum": self.maximum,
            "percentage": (
                self.percentage()
            ),
        })

        return data
