import json

from app.modules.communication.mqtt_config import (
    CommunicationMQTTConfig,
)
from app.modules.communication.mqtt_session import (
    CommunicationMQTTSession,
)


class CommunicationMQTTClient:

    def __init__(self):
        self._client = None
        self._session = None

    def available(self):
        try:
            import paho.mqtt.client  # noqa: F401

            return True

        except ImportError:
            return False

    def connect(
        self,
        config: CommunicationMQTTConfig,
    ):
        if not self.available():
            raise RuntimeError(
                "paho-mqtt is not installed"
            )

        import paho.mqtt.client as mqtt

        client = mqtt.Client(
            client_id=(
                config.client_id
                or ""
            )
        )

        if config.username:
            client.username_pw_set(
                username=config.username,
                password=config.password,
            )

        if config.tls:
            client.tls_set()

        client.connect(
            host=config.host,
            port=config.port,
            keepalive=config.keepalive,
        )

        client.loop_start()

        session = (
            CommunicationMQTTSession(
                config=config
            )
        )

        session.mark_connected()

        self._client = client
        self._session = session

        return session

    def publish(
        self,
        topic: str,
        payload: dict,
        qos: int = 0,
        retain: bool = False,
    ):
        if (
            not self._client
            or not self._session
            or not self._session.connected
        ):
            raise RuntimeError(
                "MQTT client is not connected"
            )

        result = self._client.publish(
            topic=topic,
            payload=json.dumps(
                payload
            ),
            qos=qos,
            retain=retain,
        )

        result.wait_for_publish()

        return {
            "topic": topic,
            "qos": qos,
            "retain": retain,
            "published": (
                result.rc == 0
            ),
        }

    def disconnect(self):
        if self._client:
            self._client.loop_stop()
            self._client.disconnect()

        if self._session:
            self._session.mark_disconnected()

        return True

    def session(self):
        return self._session


communication_mqtt_client = (
    CommunicationMQTTClient()
      )
