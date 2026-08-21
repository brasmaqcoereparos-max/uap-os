"""
Potenciômetro simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class PotentiometerDevice(DeviceBase):

    def __init__(self, name, pin):
        super().__init__(name)

        self.pin = pin
        self.value = 0

    def set_value(self, value):

        self.value = max(
            0,
            min(1023, int(value)),
        )

    def read(self):

        return self.value

    def update(self):
        pass

    def reset(self):

        self.value = 0
