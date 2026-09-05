from dataclasses import dataclass


@dataclass
class CommunicationMQTTSubscription:
    topic: str

    qos: int = 0

    active: bool = True

    def deactivate(self):
        self.active = False

        return True

    def to_dict(self):
        return {
            "topic": self.topic,
            "qos": self.qos,
            "active": self.active,
        }
