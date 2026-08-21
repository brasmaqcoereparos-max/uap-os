"""
Display de sete segmentos simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class SevenSegmentDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.value = 0
        self.enabled = True

    def display(
        self,
        value,
    ):

        self.value = max(
            0,
            min(
                9,
                int(value),
            ),
        )

    def clear(self):

        self.value = 0

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def update(self):
        pass

    def reset(self):

        self.value = 0
        self.enabled = True
