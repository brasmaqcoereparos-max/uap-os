from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class OLEDDevice(DeviceBase):

    def __init__(

        self,

        name,

        width=128,

        height=64,

    ):

        super().__init__(name)

        self.width = width

        self.height = height

        self.buffer = []

    def clear(self):

        self.buffer.clear()

    def draw_text(

        self,

        x,

        y,

        text,

    ):

        self.buffer.append(

            (

                x,

                y,

                text,

            )

        )

    def update(self):

        pass

    def reset(self):

        self.clear()
