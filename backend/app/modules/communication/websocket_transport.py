from typing import Any

from app.modules.communication.transport import (
    CommunicationTransport,
)
from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class WebSocketTransport(
    CommunicationTransport
):

    @property
    def name(self):
        return "websocket"

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
                    "url": destination,
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


websocket_transport = (
    WebSocketTransport()
                    )
