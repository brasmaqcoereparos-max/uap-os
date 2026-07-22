from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class LightSensorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)
        self.lux = 500

    def set_lux(
        self,
        value,
    ):
        self.lux = int(value)

    def read(self):
        return self.lux

    def update(self):
        pass

    def reset(self):
        self.lux = 500
