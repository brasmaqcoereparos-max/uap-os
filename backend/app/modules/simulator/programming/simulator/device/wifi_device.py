
from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class WiFiDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.ssid = None

    def connect(
        self,
        ssid,
    ):
        self.ssid = ssid
        self.connected = True

    def disconnect(self):
        self.connected = False
        self.ssid = None

    def is_connected(self):
        return self.connected

    def update(self):
        pass

    def reset(self):
        self.disconnect()
