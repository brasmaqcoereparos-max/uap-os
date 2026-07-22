from app.modules.simulator.programming.simulator.devices.device_base import (
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
        value,
    ):
        self.humidity = float(value)

    def read(self):
        return self.humidity

    def update(self):
        pass

    def reset(self):
        self.humidity = 50.0
