"""
Leitor QR simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class QRReaderDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(name)

        self.code = None

    def scan(self, code):

        self.code = str(code)

    def read(self):

        return self.code

    def clear(self):

        self.code = None

    def update(self):
        pass

    def reset(self):

        self.clear()
