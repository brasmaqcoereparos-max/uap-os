"""
Motor de passo simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class StepperMotorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.position = 0
        self.target_position = 0
        self.speed = 0
        self.moving = False

    def move(
        self,
        steps,
        speed=100,
    ):

        self.target_position = (
            self.position
            + int(steps)
        )

        self.speed = max(
            0,
            int(speed),
        )

        self.moving = (
            self.position
            != self.target_position
        )

    def move_to(
        self,
        position,
        speed=100,
    ):

        self.target_position = int(
            position
        )

        self.speed = max(
            0,
            int(speed),
        )

        self.moving = (
            self.position
            != self.target_position
        )

    def stop(self):

        self.target_position = (
            self.position
        )

        self.moving = False
        self.speed = 0

    def update(self):

        if not self.moving:
            return

        if self.position < self.target_position:

            self.position += 1

        elif self.position > self.target_position:

            self.position -= 1

        if self.position == self.target_position:

            self.moving = False
            self.speed = 0

    def reset(self):

        self.position = 0
        self.target_position = 0
        self.speed = 0
        self.moving = False
