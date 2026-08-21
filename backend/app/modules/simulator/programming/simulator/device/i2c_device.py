"""
Barramento I2C simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class I2CDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.devices = {}
        self.last_address = None
        self.last_data = None

    def register_device(
        self,
        address,
        device,
    ):

        self.devices[address] = device

    def write(
        self,
        address,
        data,
    ):

        if address not in self.devices:
            return False

        self.last_address = address
        self.last_data = data

        return True

    def read(
        self,
        address,
    ):

        self.last_address = address

        device = self.devices.get(address)

        if device is None:
            return None

        return device

    def update(self):
        pass

    def reset(self):

        self.last_address = None
        self.last_data = None
