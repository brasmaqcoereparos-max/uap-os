from dataclasses import dataclass
from dataclasses import field


@dataclass
class CommunicationChannel:
    name: str

    enabled: bool = True

    subscribers: set[str] = field(
        default_factory=set
    )

    def subscribe(
        self,
        subscriber_id: str,
    ):
        self.subscribers.add(
            subscriber_id
        )

        return True

    def unsubscribe(
        self,
        subscriber_id: str,
    ):
        existed = (
            subscriber_id
            in self.subscribers
        )

        self.subscribers.discard(
            subscriber_id
        )

        return existed

    def has_subscriber(
        self,
        subscriber_id: str,
    ):
        return (
            subscriber_id
            in self.subscribers
        )

    def to_dict(self):
        return {
            "name": self.name,
            "enabled": self.enabled,
            "subscribers": sorted(
                self.subscribers
            ),
              }
