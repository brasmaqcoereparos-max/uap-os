from app.modules.communication.provider_bootstrap import (
    communication_provider_bootstrap,
)
from app.modules.communication.provider_registry import (
    communication_provider_registry,
)


class CommunicationProviderManager:

    def initialize(self):
        communication_provider_bootstrap.initialize()

        return self

    def get(
        self,
        name: str,
    ):
        self.initialize()

        provider = (
            communication_provider_registry
            .get(name)
        )

        if not provider:
            raise ValueError(
                "Communication provider "
                "not found"
            )

        return provider

    def providers(self):
        self.initialize()

        return [
            {
                "name": provider.name,
                "available": (
                    provider.available()
                ),
            }
            for provider
            in communication_provider_registry
            .list_all()
        ]


communication_provider_manager = (
    CommunicationProviderManager()
)
