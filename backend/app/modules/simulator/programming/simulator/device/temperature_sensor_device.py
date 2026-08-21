"""
Sensor de temperatura simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class TemperatureSensorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.temperature = 25.0

    def set_temperature(
        self,
        temperature,
    ):

        self.temperature = float(
            temperature
        )

    def read(self):

        return self.temperature

    def update(self):
        pass

    def reset(self):

        self.temperature = 25.0
