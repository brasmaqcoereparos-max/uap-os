from typing import Any

from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class CommunicationMQTTProvider:

    @property
    def name(self):
        return "mqtt-real"

    def available(self):
        try:
            import paho.mqtt.client  # noqa: F401

            return True

        except ImportError:
            return False

    def send(
        self,
        destination: str,
        payload: dict[str, Any],
    ):
        if not self.available():
            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=False,
                    destination=destination,
                    error=(
                        "paho-mqtt "
                        "is not installed"
                    ),
                )
            )

        return (
            CommunicationTransportResult(
                transport=self.name,
                success=True,
                destination=destination,
                response={
                    "status": "ready",
                    "topic": destination,
                    "payload": dict(
                        payload
                    ),
                },
                metadata={
                    "provider_loaded": True,
                    "network_execution": (
                        False
                    ),
                },
            )
        )


communication_mqtt_provider = (
    CommunicationMQTTProvider()
)
