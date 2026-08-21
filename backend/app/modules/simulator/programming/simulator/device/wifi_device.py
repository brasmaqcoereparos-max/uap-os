"""
Dispositivo Wi-Fi simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
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
        self.ip = None

    def connect(
        self,
        ssid,
        ip=None,
    ):

        self.ssid = ssid
        self.ip = ip
        self.connected = True

    def disconnect(self):

        self.connected = False
        self.ssid = None
        self.ip = None

    def status(self):

        return {
            "connected": self.connected,
            "ssid": self.ssid,
            "ip": self.ip,
        }

    def update(self):
        pass

    def reset(self):

        self.disconnect()
