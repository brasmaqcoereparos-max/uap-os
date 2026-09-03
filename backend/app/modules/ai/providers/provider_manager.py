from app.modules.ai.providers.bootstrap import (
    ai_provider_bootstrap,
)
from app.modules.ai.providers.registry import (
    AIProviderRegistry,
    ai_provider_registry,
)


class AIProviderManager:

    def __init__(
        self,
        registry: AIProviderRegistry,
    ):
        self.registry = registry

    def initialize(self):
        ai_provider_bootstrap.initialize()

        return self

    def get(
        self,
        name: str | None = None,
    ):
        self.initialize()

        if name:
            provider = (
                self.registry.get(
                    name
                )
            )

        else:
            provider = (
                self.registry.default()
            )

        if not provider:
            raise ValueError(
                "AI provider not found"
            )

        if not provider.available():
            raise RuntimeError(
                "AI provider unavailable"
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
                "default": (
                    self.registry.default()
                    is provider
                ),
            }
            for provider
            in self.registry.list_all()
        ]


ai_provider_manager = (
    AIProviderManager(
        registry=ai_provider_registry
    )
)
