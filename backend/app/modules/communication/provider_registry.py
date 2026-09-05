class CommunicationProviderRegistry:

    def __init__(self):
        self._providers = {}

    def register(
        self,
        provider,
    ):
        self._providers[
            provider.name
        ] = provider

        return provider

    def get(
        self,
        name: str,
    ):
        return self._providers.get(
            name
        )

    def list_all(self):
        return list(
            self._providers.values()
        )

    def available(self):
        return [
            provider
            for provider
            in self._providers.values()
            if provider.available()
        ]

    def clear(self):
        self._providers.clear()


communication_provider_registry = (
    CommunicationProviderRegistry()
  )
