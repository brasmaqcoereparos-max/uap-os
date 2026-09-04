import uuid
from typing import Any

from app.modules.communication.channel_registry import (
    communication_channel_registry,
)
from app.modules.communication.message_envelope import (
    CommunicationMessageEnvelope,
)
from app.modules.communication.message_router import (
    communication_message_router,
)
from app.modules.communication.subscriber import (
    CommunicationSubscriber,
)
from app.modules.communication.subscriber_registry import (
    communication_subscriber_registry,
)


class CommunicationMessageBus:

    def subscribe(
        self,
        topic: str,
        subscriber_id: str,
        handler,
    ):
        subscriber = (
            CommunicationSubscriber(
                id=subscriber_id,
                handler=handler,
            )
        )

        communication_subscriber_registry
        .register(
            subscriber
        )

        channel = (
            communication_channel_registry
            .get_or_create(
                topic
            )
        )

        channel.subscribe(
            subscriber_id
        )

        return subscriber

    def unsubscribe(
        self,
        topic: str,
        subscriber_id: str,
    ):
        channel = (
            communication_channel_registry
            .get(topic)
        )

        if channel:
            channel.unsubscribe(
                subscriber_id
            )

        communication_subscriber_registry
        .remove(
            subscriber_id
        )

        return True

    def publish(
        self,
        topic: str,
        source: str,
        payload: (
            dict[str, Any] | None
        ) = None,
        target: str | None = None,
        correlation_id: (
            str | None
        ) = None,
    ):
        envelope = (
            CommunicationMessageEnvelope(
                id=str(uuid.uuid4()),
                topic=topic,
                source=source,
                payload=dict(
                    payload or {}
                ),
                target=target,
                correlation_id=(
                    correlation_id
                ),
            )
        )

        return (
            communication_message_router
            .route(envelope)
        )


communication_message_bus = (
    CommunicationMessageBus()
      )
