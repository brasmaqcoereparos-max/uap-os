from typing import Any

from app.modules.communication.transport import (
    CommunicationTransport,
)
from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class SerialTransport(
    CommunicationTransport
):

    @property
    def name(self):
        return "serial"

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
                    "port": destination,
                    "payload": dict(
                        payload
                    ),
                },
                metadata={
                    "physical_execution": (
                        False
                    ),
                },
            )
        )


serial_transport = (
    SerialTransport()
                  )
