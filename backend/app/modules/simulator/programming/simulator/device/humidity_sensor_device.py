from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class HumiditySensorDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
        humidity=50.0,
    ):
        super().__init__(
            name=name,
            category="sensor",
            description=(
                "Sensor de umidade"
            ),
            icon="droplet",
        )

        self.humidity = 0.0

        self.set_humidity(
            humidity
        )

    def set_humidity(
        self,
        humidity,
    ):
        value = max(
            0.0,
            min(
                100.0,
                float(humidity),
            ),
        )

        self.humidity = value

        return self.humidity

    def read(self):
        return self.humidity

    def update(self):
        return self.humidity

    def reset(self):
        self.humidity = 50.0
        return self.humidity

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "humidity": (
                self.humidity
            ),
            "unit": "%",
        })

        return data
