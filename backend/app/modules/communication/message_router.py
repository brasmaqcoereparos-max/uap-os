from app.modules.communication.channel_registry import (
    communication_channel_registry,
)
from app.modules.communication.delivery_result import (
    CommunicationDeliveryResult,
)
from app.modules.communication.message_envelope import (
    CommunicationMessageEnvelope,
)
from app.modules.communication.subscriber_registry import (
    communication_subscriber_registry,
)


class CommunicationMessageRouter:

    def route(
        self,
        envelope: (
            CommunicationMessageEnvelope
        ),
    ):
        channel = (
            communication_channel_registry
            .get(
                envelope.topic
            )
        )

        if not channel:
            return (
                CommunicationDeliveryResult(
                    delivered=False,
                    topic=envelope.topic,
                )
            )

        recipients = []
        results = {}
        errors = {}

        for subscriber_id in (
            channel.subscribers
        ):
            subscriber = (
                communication_subscriber_registry
                .get(
                    subscriber_id
                )
            )

            if not subscriber:
                continue

            if envelope.target:
                if (
                    subscriber_id
                    != envelope.target
                ):
                    continue

            recipients.append(
                subscriber_id
            )

            try:
                result = (
                    subscriber.handle(
                        envelope.to_dict()
                    )
                )

                results[
                    subscriber_id
                ] = result

            except Exception as exc:
                errors[
                    subscriber_id
                ] = str(exc)

        return (
            CommunicationDeliveryResult(
                delivered=(
                    bool(recipients)
                    and not errors
                ),
                topic=envelope.topic,
                recipients=recipients,
                results=results,
                errors=errors,
            )
        )


communication_message_router = (
    CommunicationMessageRouter()
)
