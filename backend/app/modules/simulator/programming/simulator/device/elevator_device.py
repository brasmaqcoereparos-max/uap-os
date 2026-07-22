from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class ElevatorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.level = 0

    def move_to(
        self,
        level,
    ):

        self.level = int(level)

    def update(self):

        pass

    def reset(self):

        self.level = 0
