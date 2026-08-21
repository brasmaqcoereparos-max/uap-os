"""
Leitor RFID simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class RFIDReaderDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(name)

        self.uid = None
        self.data = {}

    def scan(self, uid):

        self.uid = str(uid)

    def read_uid(self):

        return self.uid

    def write_data(self, key, value):

        self.data[key] = value

    def read_data(self, key):

        return self.data.get(key)

    def clear(self):

        self.uid = None
        self.data.clear()

    def update(self):
        pass

    def reset(self):

        self.clear()
