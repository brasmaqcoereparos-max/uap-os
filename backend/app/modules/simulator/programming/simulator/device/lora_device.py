from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class LoRaDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.messages = []

    def send(
        self,
        message,
    ):
        self.messages.append(message)

    def receive(self):

        if self.messages:

            return self.messages.pop(0)

        return None

    def update(self):

        pass

    def reset(self):

        self.messages.clear()
