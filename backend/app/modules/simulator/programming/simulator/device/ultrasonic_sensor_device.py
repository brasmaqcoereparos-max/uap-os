from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class UltrasonicSensorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)
        self.distance = 100.0

    def set_distance(
        self,
        distance,
    ):
        self.distance = float(distance)

    def read(self):
        return self.distance

    def update(self):
        pass

    def reset(self):
        self.distance = 100.0
