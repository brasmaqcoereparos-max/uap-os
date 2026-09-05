import json

from app.modules.communication.inbound_message import (
    CommunicationInboundMessage,
)
from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)
from app.modules.communication.mqtt_client import (
    communication_mqtt_client,
)
from app.modules.communication.mqtt_subscription import (
    CommunicationMQTTSubscription,
)


class CommunicationMQTTReceiver:

    def __init__(self):
        self._subscriptions: dict[
            str,
            CommunicationMQTTSubscription,
        ] = {}

    def subscribe(
        self,
        topic: str,
        qos: int = 0,
    ):
        client = getattr(
            communication_mqtt_client,
            "_client",
            None,
        )

        if client is None:
            raise RuntimeError(
                "MQTT client is not connected"
            )

        subscription = (
            CommunicationMQTTSubscription(
                topic=topic,
                qos=qos,
            )
        )

        def on_message(
            mqtt_client,
            userdata,
            message,
        ):
            raw = message.payload

            try:
                payload = json.loads(
                    raw.decode(
                        "utf-8"
                    )
                )

            except Exception:
                payload = raw.decode(
                    "utf-8",
                    errors="replace",
                )

            communication_inbound_queue.push(
                CommunicationInboundMessage(
                    source="mqtt",
                    channel=(
                        message.topic
                    ),
                    payload=payload,
                    metadata={
                        "qos": (
                            message.qos
                        ),
                        "retain": (
                            message.retain
                        ),
                    },
                )
            )

        client.on_message = on_message

        client.subscribe(
            topic,
            qos=qos,
        )

        self._subscriptions[
            topic
        ] = subscription

        return subscription

    def unsubscribe(
        self,
        topic: str,
    ):
        client = getattr(
            communication_mqtt_client,
            "_client",
            None,
        )

        if client is None:
            return False

        client.unsubscribe(
            topic
        )

        subscription = (
            self._subscriptions.get(
                topic
            )
        )

        if subscription:
            subscription.deactivate()

        return True

    def list_all(self):
        return [
            subscription.to_dict()
            for subscription
            in self._subscriptions.values()
        ]


communication_mqtt_receiver = (
    CommunicationMQTTReceiver()
)
