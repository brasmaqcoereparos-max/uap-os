"""
Sensor de umidade simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class HumiditySensorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.humidity = 50.0

    def set_humidity(
        self,
        humidity,
    ):

        self.humidity = max(
            0.0,
            min(
                100.0,
                float(humidity),
            ),
        )

    def read(self):

        return self.humidity

    def update(self):
        pass

    def reset(self):

        self.humidity = 50.0
