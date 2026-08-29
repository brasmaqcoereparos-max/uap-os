from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class UltrasonicSensorDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
        distance=0.0,
        unit="cm",
    ):
        super().__init__(
            name=name,
            category="sensor",
            description=(
                "Sensor ultrassônico "
                "de distância"
            ),
            icon="ruler",
        )

        self.distance = max(
            0.0,
            float(distance),
        )

        self.unit = str(unit)

    def set_distance(
        self,
        distance,
    ):
        if not self.enabled:
            return False

        self.distance = max(
            0.0,
            float(distance),
        )

        return self.distance

    def read(self):
        return self.distance

    def measure(self):
        return self.distance

    def is_near(
        self,
        threshold,
    ):
        return (
            self.distance
            <= float(threshold)
        )

    def update(self):
        return self.distance

    def reset(self):
        self.distance = 0.0
        return self.distance

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "distance": (
                self.distance
            ),
            "unit": self.unit,
        })

        return data
