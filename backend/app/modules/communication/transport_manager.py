from typing import Any

from app.modules.communication.transport_bootstrap import (
    communication_transport_bootstrap,
)
from app.modules.communication.transport_registry import (
    communication_transport_registry,
)


class CommunicationTransportManager:

    def initialize(self):
        communication_transport_bootstrap.initialize()

        return self

    def get(
        self,
        transport_name: (
            str | None
        ) = None,
    ):
        self.initialize()

        if transport_name:
            transport = (
                communication_transport_registry
                .get(
                    transport_name
                )
            )

        else:
            transport = (
                communication_transport_registry
                .default()
            )

        if not transport:
            raise ValueError(
                "Communication transport "
                "not found"
            )

        if not transport.available():
            raise RuntimeError(
                "Communication transport "
                "unavailable"
            )

        return transport

    def send(
        self,
        destination: str,
        payload: dict[
            str,
            Any,
        ],
        transport_name: (
            str | None
        ) = None,
    ):
        transport = self.get(
            transport_name
        )

        return transport.send(
            destination=destination,
            payload=payload,
        )

    def transports(self):
        self.initialize()

        default_transport = (
            communication_transport_registry
            .default()
        )

        return [
            {
                "name": transport.name,
                "available": (
                    transport.available()
                ),
                "default": (
                    default_transport
                    is transport
                ),
            }
            for transport
            in communication_transport_registry
            .list_all()
        ]


communication_transport_manager = (
    CommunicationTransportManager()
)
