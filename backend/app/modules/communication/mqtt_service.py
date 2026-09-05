from app.modules.communication.mqtt_client import (
    communication_mqtt_client,
)
from app.modules.communication.mqtt_config import (
    CommunicationMQTTConfig,
)


class CommunicationMQTTService:

    def connect(
        self,
        host: str,
        port: int = 1883,
        username: str | None = None,
        password: str | None = None,
        keepalive: int = 60,
        tls: bool = False,
        client_id: str | None = None,
    ):
        config = (
            CommunicationMQTTConfig(
                host=host,
                port=port,
                username=username,
                password=password,
                keepalive=keepalive,
                tls=tls,
                client_id=client_id,
            )
        )

        session = (
            communication_mqtt_client
            .connect(config)
        )

        return session.to_dict()

    def publish(
        self,
        topic: str,
        payload: dict,
        qos: int = 0,
        retain: bool = False,
    ):
        return (
            communication_mqtt_client
            .publish(
                topic=topic,
                payload=payload,
                qos=qos,
                retain=retain,
            )
        )

    def disconnect(self):
        return (
            communication_mqtt_client
            .disconnect()
        )

    def status(self):
        session = (
            communication_mqtt_client
            .session()
        )

        return (
            session.to_dict()
            if session
            else {
                "connected": False,
                "config": None,
            }
        )


communication_mqtt_service = (
    CommunicationMQTTService()
)
