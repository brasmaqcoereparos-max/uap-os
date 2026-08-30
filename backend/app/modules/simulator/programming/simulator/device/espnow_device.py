"""
Dispositivo ESP-NOW simulado do UAP.
"""

from app.modules.simulator.programming.simulator.device.device_base import (
    DeviceBase,
)


class ESPNowDevice(DeviceBase):

    def __init__(self, name):
        super().__init__(
            name=name,
            category="communication",
            description="Comunicação ESP-NOW simulada",
            icon="wifi",
        )

        self.connected = False
        self.peer = None
        self.peers = set()

        self.messages = []
        self.received_messages = []

        self.sent_count = 0
        self.received_count = 0

    def connect(self, peer):
        if not self.enabled:
            return False

        self.peer = str(peer)
        self.peers.add(self.peer)
        self.connected = True
        return True

    def disconnect(self):
        self.peer = None
        self.connected = False
        return True

    def add_peer(self, peer):
        peer = str(peer)
        self.peers.add(peer)
        return peer

    def remove_peer(self, peer):
        self.peers.discard(str(peer))

        if self.peer == str(peer):
            self.disconnect()

        return True

    def send(self, message):
        if not self.enabled or not self.connected:
            return False

        self.messages.append(message)
        self.sent_count += 1
        return True

    def receive(self):
        if self.received_messages:
            message = self.received_messages.pop(0)
            self.received_count += 1
            return message

        if self.messages:
            message = self.messages.pop(0)
            self.received_count += 1
            return message

        return None

    def inject_received(self, message):
        self.received_messages.append(message)
        return True

    def update(self):
        return {
            "connected": self.connected,
            "peer": self.peer,
            "peers": list(self.peers),
            "pending": (
                len(self.messages)
                + len(self.received_messages)
            ),
        }

    def reset(self):
        self.messages.clear()
        self.received_messages.clear()
        self.peers.clear()
        self.sent_count = 0
        self.received_count = 0
        self.disconnect()
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "connected": self.connected,
            "peer": self.peer,
            "peers": list(self.peers),
            "sent_count": self.sent_count,
            "received_count": self.received_count,
        })
        return data
