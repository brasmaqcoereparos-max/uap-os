from app.modules.communication.http_transport import (
    http_transport,
)
from app.modules.communication.memory_transport import (
    memory_transport,
)
from app.modules.communication.mqtt_transport import (
    mqtt_transport,
)
from app.modules.communication.serial_transport import (
    serial_transport,
)
from app.modules.communication.transport_registry import (
    communication_transport_registry,
)
from app.modules.communication.websocket_transport import (
    websocket_transport,
)


class CommunicationTransportBootstrap:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if self._initialized:
            return (
                communication_transport_registry
            )

        transports = [
            memory_transport,
            http_transport,
            websocket_transport,
            mqtt_transport,
            serial_transport,
        ]

        for transport in transports:
            if not (
                communication_transport_registry
                .get(
                    transport.name
                )
            ):
                communication_transport_registry
                .register(
                    transport,
                    default=(
                        transport.name
                        == "memory"
                    ),
                )

        self._initialized = True

        return (
            communication_transport_registry
        )


communication_transport_bootstrap = (
    CommunicationTransportBootstrap()
  )
