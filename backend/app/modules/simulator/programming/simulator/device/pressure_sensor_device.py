from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class PressureSensorDevice(
    DeviceBase
):

    def __init__(
        self,
        name,
        pressure=0.0,
        unit="kPa",
    ):
        super().__init__(
            name=name,
            category="sensor",
            description=(
                "Sensor de pressão"
            ),
            icon="gauge",
        )

        self.pressure = float(
            pressure
        )

        self.unit = str(unit)

    def set_pressure(
        self,
        pressure,
    ):
        if not self.enabled:
            return False

        self.pressure = float(
            pressure
        )

        return self.pressure

    def read(self):
        return self.pressure

    def update(self):
        return self.pressure

    def reset(self):
        self.pressure = 0.0
        return self.pressure

    def to_dict(self):
        data = super().to_dict()

        data.update({
            "pressure": (
                self.pressure
            ),
            "unit": self.unit,
        })

        return data
