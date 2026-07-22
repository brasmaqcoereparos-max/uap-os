from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class PressureSensorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)
        self.pressure = 1013.25

    def set_pressure(
        self,
        value,
    ):
        self.pressure = float(value)

    def read(self):
        return self.pressure

    def update(self):
        pass

    def reset(self):
        self.pressure = 1013.25
