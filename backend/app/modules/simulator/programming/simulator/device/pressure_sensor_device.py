"""
Sensor de pressão simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class PressureSensorDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(name)

        self.pressure = 0.0

    def set_pressure(self, pressure):

        self.pressure = float(pressure)

    def read(self):

        return self.pressure

    def update(self):
        pass

    def reset(self):

        self.pressure = 0.0
