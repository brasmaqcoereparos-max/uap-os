"""
Sensor ultrassônico simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class UltrasonicSensorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.distance = 0.0

    def set_distance(
        self,
        distance,
    ):

        self.distance = max(
            0.0,
            float(distance),
        )

    def read(self):

        return self.distance

    def measure(self):

        return self.distance

    def update(self):
        pass

    def reset(self):

        self.distance = 0.0
