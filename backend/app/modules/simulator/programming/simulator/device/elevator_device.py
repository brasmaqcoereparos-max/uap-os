
from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ElevatorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.level = 0
        self.target_level = 0
        self.moving = False

    def move_to(
        self,
        level,
    ):
        self.target_level = int(level)
        self.moving = (
            self.level
            != self.target_level
        )

    def update(self):

        if not self.moving:
            return

        if self.level < self.target_level:
            self.level += 1

        elif self.level > self.target_level:
            self.level -= 1

        if self.level == self.target_level:
            self.moving = False

    def stop(self):
        self.target_level = self.level
        self.moving = False

    def reset(self):
        self.level = 0
        self.target_level = 0
        self.moving = False
