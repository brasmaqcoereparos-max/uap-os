from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class I2CDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.devices = {}

    def register(
        self,
        address,
        device,
    ):
        self.devices[address] = device

    def read(
        self,
        address,
    ):
        return self.devices.get(address)

    def update(self):
        pass

    def reset(self):
        self.devices.clear()
