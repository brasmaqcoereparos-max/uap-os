"""
Dispositivo ESP-NOW para o simulador UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ESPNowDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.peer = None
        self.messages = []

    def connect(
        self,
        peer,
    ):
        self.peer = peer
        self.connected = True

    def disconnect(self):
        self.peer = None
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
        self.disconnect()
