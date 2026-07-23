from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class UARTDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.buffer = []

    def write(
        self,
        data,
    ):
        self.buffer.append(data)

    def read(self):

        if self.buffer:

            return self.buffer.pop(0)

        return None

    def update(self):
        pass

    def reset(self):
        self.buffer.clear()
