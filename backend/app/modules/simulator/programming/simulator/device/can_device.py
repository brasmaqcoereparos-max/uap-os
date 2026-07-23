from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class CANDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.frames = []

    def send(
        self,
        frame,
    ):
        self.frames.append(frame)

    def receive(self):

        if self.frames:

            return self.frames.pop(0)

        return None

    def update(self):
        pass

    def reset(self):
        self.frames.clear()
