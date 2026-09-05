from dataclasses import dataclass


@dataclass
class CommunicationWebSocketSession:
    url: str

    connected: bool = False

    def connect(self):
        self.connected = True

        return True

    def disconnect(self):
        self.connected = False

        return True

    def to_dict(self):
        return {
            "url": self.url,
            "connected": (
                self.connected
            ),
        }
