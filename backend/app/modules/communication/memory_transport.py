from typing import Any

from app.modules.communication.transport import (
    CommunicationTransport,
)
from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class MemoryTransport(
    CommunicationTransport
):

    def __init__(self):
        self._messages: list[
            dict[str, Any]
        ] = []

    @property
    def name(self):
        return "memory"

    def available(self):
        return True

    def send(
        self,
        destination: str,
        payload: dict[str, Any],
    ):
        message = {
            "destination": (
                destination
            ),
            "payload": dict(
                payload
            ),
        }

        self._messages.append(
            message
        )

        return (
            CommunicationTransportResult(
                transport=self.name,
                success=True,
                destination=(
                    destination
                ),
                response=message,
                metadata={
                    "simulation": True,
                },
            )
        )

    def messages(self):
        return list(
            self._messages
        )

    def clear(self):
        self._messages.clear()


memory_transport = (
    MemoryTransport()
)
