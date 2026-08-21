"""
UART simulada do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class UARTDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.connected = False
        self.baudrate = 9600
        self.buffer = []

    def connect(
        self,
        baudrate=9600,
    ):

        self.baudrate = int(
            baudrate
        )

        self.connected = True

    def disconnect(self):

        self.connected = False

    def write(
        self,
        data,
    ):

        if not self.connected:
            return False

        self.buffer.append(data)

        return True

    def read(self):

        if not self.buffer:
            return None

        return self.buffer.pop(0)

    def update(self):
        pass

    def reset(self):

        self.buffer.clear()
        self.disconnect()
