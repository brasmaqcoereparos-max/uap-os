from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class LCD16x2Device(DeviceBase):

    def __init__(

        self,

        name,

    ):

        super().__init__(name)

        self.rows = [

            " " * 16,

            " " * 16,

        ]

    def clear(self):

        self.rows = [

            " " * 16,

            " " * 16,

        ]

    def write(

        self,

        row,

        text,

    ):

        if row < 0 or row > 1:

            return

        self.rows[row] = text[:16].ljust(16)

    def update(self):

        pass

    def reset(self):

        self.clear()
