from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class ModbusTCPDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def update(self):

        pass

    def reset(self):

        self.disconnect()
