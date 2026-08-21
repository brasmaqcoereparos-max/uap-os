"""
Barramento SPI simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class SPIDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.devices = {}
        self.last_transfer = None

    def register_device(
        self,
        chip_select,
        device,
    ):

        self.devices[
            chip_select
        ] = device

    def transfer(
        self,
        chip_select,
        data,
    ):

        if chip_select not in self.devices:
            return None

        self.last_transfer = {
            "chip_select": chip_select,
            "data": data,
        }

        return data

    def update(self):
        pass

    def reset(self):

        self.last_transfer = None
