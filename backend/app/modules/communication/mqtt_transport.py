from typing import Any

from app.modules.communication.transport import (
    CommunicationTransport,
)
from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class MQTTTransport(
    CommunicationTransport
):

    @property
    def name(self):
        return "mqtt"

    def available(self):
        return True

    def send(
        self,
        destination: str,
        payload: dict[str, Any],
    ):
        return (
            CommunicationTransportResult(
                transport=self.name,
                success=True,
                destination=(
                    destination
                ),
                response={
                    "status": "prepared",
                    "topic": destination,
                    "payload": dict(
                        payload
                    ),
                },
                metadata={
                    "network_execution": (
                        False
                    ),
                },
            )
        )


mqtt_transport = (
    MQTTTransport()
)
