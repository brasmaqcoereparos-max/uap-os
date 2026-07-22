from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class ConveyorDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.running = False

        self.speed = 0

    def start(
        self,
        speed=100,
    ):

        self.running = True

        self.speed = speed

    def stop(self):

        self.running = False

        self.speed = 0

    def update(self):

        pass

    def reset(self):

        self.stop()
