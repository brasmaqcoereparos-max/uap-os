"""
Dispositivo LoRa simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class LoRaDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.frequency = 0
        self.messages = []

    def connect(
        self,
        frequency,
    ):

        self.frequency = frequency
        self.connected = True

    def disconnect(self):

        self.connected = False

    def send(
        self,
        message,
    ):

        if not self.connected:
            return False

        self.messages.append(message)

        return True

    def receive(self):

        if not self.messages:
            return None

        return self.messages.pop(0)

    def update(self):
        pass

    def reset(self):

        self.messages.clear()
        self.frequency = 0
        self.disconnect()
