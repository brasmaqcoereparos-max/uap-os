from app.modules.communication.http_provider import (
    communication_http_provider,
)
from app.modules.communication.mqtt_provider import (
    communication_mqtt_provider,
)
from app.modules.communication.provider_registry import (
    communication_provider_registry,
)
from app.modules.communication.serial_provider import (
    communication_serial_provider,
)


class CommunicationProviderBootstrap:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if self._initialized:
            return (
                communication_provider_registry
            )

        providers = [
            communication_http_provider,
            communication_mqtt_provider,
            communication_serial_provider,
        ]

        for provider in providers:
            if not (
                communication_provider_registry
                .get(
                    provider.name
                )
            ):
                communication_provider_registry
                .register(provider)

        self._initialized = True

        return (
            communication_provider_registry
        )


communication_provider_bootstrap = (
    CommunicationProviderBootstrap()
              )
