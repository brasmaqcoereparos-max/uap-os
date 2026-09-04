from app.modules.communication.transport import (
    CommunicationTransport,
)


class CommunicationTransportRegistry:

    def __init__(self):
        self._transports: dict[
            str,
            CommunicationTransport,
        ] = {}

        self._default: (
            str | None
        ) = None

    def register(
        self,
        transport: CommunicationTransport,
        default: bool = False,
    ):
        self._transports[
            transport.name
        ] = transport

        if (
            default
            or self._default is None
        ):
            self._default = (
                transport.name
            )

        return transport

    def get(
        self,
        name: str,
    ):
        return self._transports.get(
            name
        )

    def default(self):
        if self._default is None:
            return None

        return self.get(
            self._default
        )

    def set_default(
        self,
        name: str,
    ):
        if (
            name
            not in self._transports
        ):
            raise ValueError(
                "Communication transport "
                "not found"
            )

        self._default = name

        return self.get(name)

    def list_all(self):
        return list(
            self._transports.values()
        )


communication_transport_registry = (
    CommunicationTransportRegistry()
      )
