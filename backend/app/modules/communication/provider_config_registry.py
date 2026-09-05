from app.modules.communication.provider_config import (
    CommunicationProviderConfig,
)


class CommunicationProviderConfigRegistry:

    def __init__(self):
        self._configs: dict[
            str,
            CommunicationProviderConfig,
        ] = {}

    def register(
        self,
        config: (
            CommunicationProviderConfig
        ),
    ):
        self._configs[
            config.name
        ] = config

        return config

    def get(
        self,
        name: str,
    ):
        return self._configs.get(
            name
        )

    def remove(
        self,
        name: str,
    ):
        return self._configs.pop(
            name,
            None,
        )

    def list_all(self):
        return list(
            self._configs.values()
        )


communication_provider_config_registry = (
    CommunicationProviderConfigRegistry()
)
