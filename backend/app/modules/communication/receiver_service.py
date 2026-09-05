from app.modules.communication.inbound_queue import (
    communication_inbound_queue,
)
from app.modules.communication.mqtt_receiver import (
    communication_mqtt_receiver,
)
from app.modules.communication.websocket_receiver import (
    communication_websocket_receiver,
)


class CommunicationReceiverService:

    def mqtt_subscribe(
        self,
        topic: str,
        qos: int = 0,
    ):
        return (
            communication_mqtt_receiver
            .subscribe(
                topic=topic,
                qos=qos,
            )
            .to_dict()
        )

    def mqtt_unsubscribe(
        self,
        topic: str,
    ):
        return (
            communication_mqtt_receiver
            .unsubscribe(
                topic
            )
        )

    def mqtt_subscriptions(
        self,
    ):
        return (
            communication_mqtt_receiver
            .list_all()
        )

    def queue_status(self):
        return (
            communication_inbound_queue
            .snapshot()
        )

    def pop_message(self):
        message = (
            communication_inbound_queue
            .pop()
        )

        if not message:
            return None

        return message.to_dict()

    def websocket_status(self):
        return (
            communication_websocket_receiver
            .status()
        )


communication_receiver_service = (
    CommunicationReceiverService()
)
