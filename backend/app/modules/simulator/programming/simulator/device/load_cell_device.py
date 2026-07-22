from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class LoadCellDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.weight = 0.0

    def set_weight(
        self,
        weight,
    ):

        self.weight = float(weight)

    def read(self):

        return self.weight

    def update(self):

        pass

    def reset(self):

        self.weight = 0.0
