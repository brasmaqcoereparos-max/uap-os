from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class StepperMotorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.position = 0

    def move(
        self,
        steps,
    ):

        self.position += int(steps)

    def update(self):

        pass

    def reset(self):

        self.position = 0
