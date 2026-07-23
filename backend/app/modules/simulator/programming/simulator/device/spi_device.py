from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class SPIDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.selected = None

    def select(
        self,
        device,
    ):
        self.selected = device

    def transfer(
        self,
        data,
    ):
        return data

    def update(self):
        pass

    def reset(self):
        self.selected = None
