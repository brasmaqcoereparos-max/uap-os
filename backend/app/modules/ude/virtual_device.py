from app.modules.ude.device import Device
from app.modules.ude.device_types import DeviceType


class VirtualDevice(Device):

    def __init__(
        self,
        name,
    ):

        super().__init__(
            name,
            DeviceType.VIRTUAL.value,
        )

        self.state = {}

    def set(
        self,
        name,
        value,
    ):

        self.state[name] = value

    def get(
        self,
        name,
        default=None,
    ):

        return self.state.get(
            name,
            default,
        )"""
Universal Device Engine
"""
