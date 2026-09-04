from app.modules.communication.subscriber import (
    CommunicationSubscriber,
)


class CommunicationSubscriberRegistry:

    def __init__(self):
        self._subscribers: dict[
            str,
            CommunicationSubscriber,
        ] = {}

    def register(
        self,
        subscriber: (
            CommunicationSubscriber
        ),
    ):
        self._subscribers[
            subscriber.id
        ] = subscriber

        return subscriber

    def get(
        self,
        subscriber_id: str,
    ):
        return self._subscribers.get(
            subscriber_id
        )

    def remove(
        self,
        subscriber_id: str,
    ):
        return self._subscribers.pop(
            subscriber_id,
            None,
        )

    def list_all(self):
        return list(
            self._subscribers.values()
        )

    def clear(self):
        self._subscribers.clear()


communication_subscriber_registry = (
    CommunicationSubscriberRegistry()
)
