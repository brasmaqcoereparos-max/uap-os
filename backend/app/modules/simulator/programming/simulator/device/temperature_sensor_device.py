from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class TemperatureSensorDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
        temperature=25.0,
        unit="°C",
    ):
        super().__init__(
            name=name,
            category="sensor",
            description=(
                "Sensor de temperatura"
            ),
            icon="thermometer",
        )

        self.temperature = float(
            temperature
        )

        self.unit = str(unit)

    def set_temperature(
        self,
        temperature,
    ):
        if not self.enabled:
            return False

        self.temperature = float(
            temperature
        )

        return self.temperature

    def read(self):
        return self.temperature

    def update(self):
        return self.temperature

    def reset(self):
        self.temperature = 25.0
        return self.temperature

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "temperature": (
                self.temperature
            ),
            "unit": self.unit,
        })

        return data
