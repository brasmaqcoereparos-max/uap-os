from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class LightSensorDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
        value=0,
        minimum=0,
        maximum=1023,
    ):
        super().__init__(
            name=name,
            category="sensor",
            description=(
                "Sensor de luminosidade"
            ),
            icon="sun",
        )

        self.minimum = int(minimum)
        self.maximum = int(maximum)

        if self.minimum >= self.maximum:
            raise ValueError(
                "Faixa de luminosidade inválida."
            )

        self.value = self.minimum

        self.set_value(value)

    def set_value(self, value):
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

    def percentage(self):
        span = (
            self.maximum
            - self.minimum
        )

        if span <= 0:
            return 0.0

        return round(
            (
                (
                    self.value
                    - self.minimum
                )
                / span
            )
            * 100,
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
            "value": self.value,
            "minimum": self.minimum,
            "maximum": self.maximum,
            "percentage": (
                self.percentage()
            ),
        })

        return data
