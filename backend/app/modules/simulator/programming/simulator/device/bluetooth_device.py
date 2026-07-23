
from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class BluetoothDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.device = None

    def connect(
        self,
        device,
    ):
        self.device = device
        self.connected = True

    def disconnect(self):
        self.connected = False
        self.device = None

    def update(self):
        pass

    def reset(self):
        self.disconnect()
