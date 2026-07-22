from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class RFIDReaderDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.tag = None

    def set_tag(
        self,
        tag,
    ):

        self.tag = tag

    def read(self):

        return self.tag

    def clear(self):

        self.tag = None

    def update(self):

        pass

    def reset(self):

        self.clear()
