from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class SevenSegmentDevice(DeviceBase):

    def __init__(

        self,

        name,

    ):

        super().__init__(name)

        self.value = 0

    def display(

        self,

        value,

    ):

        self.value = int(value)

    def update(self):

        pass

    def reset(self):

        self.value = 0
