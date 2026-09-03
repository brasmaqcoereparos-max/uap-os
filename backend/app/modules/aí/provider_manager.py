from app.modules.ai.mock_provider import (
    ai_mock_provider,
)
from app.modules.ai.provider_registry import (
    ai_provider_registry,
)


class AIProviderManager:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            ai_provider_registry.register(
                ai_mock_provider,
                default=True,
            )

            self._initialized = True

        return self

    def get(
        self,
        name: str | None = None,
    ):
        self.initialize()

        if name:
            provider = (
                ai_provider_registry
                .get(name)
            )
        else:
            provider = (
                ai_provider_registry
                .default()
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
            }
            for provider
            in ai_provider_registry
            .list_all()
        ]


ai_provider_manager = (
    AIProviderManager()
)
