from app.modules.simulator.programming.simulator.devices.device_base import (
    DeviceBase,
)


class ESPNowDevice(DeviceBase):

    def __init__(
        self,
        name,
    ):
        super().__init__(name)

        self.peers = []

    def add_peer(
        self,
        peer,
    ):
        self.peers.append(peer)

    def update(self):

        pass

    def reset(self):

        self.peers.clear()
