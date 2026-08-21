"""
Display OLED simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class OLEDDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(name)

        self.lines = []
        self.text = ""

    def write(self, text):

        self.text = str(text)

    def clear(self):

        self.text = ""

        self.lines.clear()

    def add_line(self, text):

        self.lines.append(str(text))

    def get_text(self):

        return self.text

    def update(self):
        pass

    def reset(self):
        self.clear()
