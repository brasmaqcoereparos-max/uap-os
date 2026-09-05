from dataclasses import dataclass

from app.modules.communication.mqtt_config import (
    CommunicationMQTTConfig,
)


@dataclass
class CommunicationMQTTSession:
    config: CommunicationMQTTConfig

    connected: bool = False

    def mark_connected(self):
        self.connected = True

        return True

    def mark_disconnected(self):
        self.connected = False

        return True

    def to_dict(self):
        return {
            "connected": self.connected,
            "config": (
                self.config.to_dict()
            ),
        }
