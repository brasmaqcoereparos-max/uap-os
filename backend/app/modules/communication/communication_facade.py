from typing import Any

from app.modules.communication.channel_registry import (
    communication_channel_registry,
)
from app.modules.communication.message_bus import (
    communication_message_bus,
)


class CommunicationFacade:

    def publish(
        self,
        topic: str,
        source: str,
        payload: (
            dict[str, Any] | None
        ) = None,
        target: str | None = None,
    ):
        return (
            communication_message_bus
            .publish(
                topic=topic,
                source=source,
                payload=payload,
                target=target,
            )
        )

    def subscribe(
        self,
        topic: str,
        subscriber_id: str,
        handler,
    ):
        return (
            communication_message_bus
            .subscribe(
                topic=topic,
                subscriber_id=(
                    subscriber_id
                ),
                handler=handler,
            )
        )

    def unsubscribe(
        self,
        topic: str,
        subscriber_id: str,
    ):
        return (
            communication_message_bus
            .unsubscribe(
                topic=topic,
                subscriber_id=(
                    subscriber_id
                ),
            )
        )

    def channels(self):
        return [
            channel.to_dict()
            for channel
            in communication_channel_registry
            .list_all()
        ]


communication_facade = (
    CommunicationFacade()
)
