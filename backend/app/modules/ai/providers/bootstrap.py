from app.modules.ai.providers.mock import (
    MockProvider,
)
from app.modules.ai.providers.openai_provider import (
    openai_provider,
)
from app.modules.ai.providers.registry import (
    ai_provider_registry,
)


class AIProviderBootstrap:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if self._initialized:
            return (
                ai_provider_registry
            )

        existing_mock = (
            ai_provider_registry.get(
                "mock"
            )
        )

        if not existing_mock:
            ai_provider_registry.register(
                MockProvider()
            )

        if not (
            ai_provider_registry.get(
                "openai"
            )
        ):
            ai_provider_registry.register(
                openai_provider
            )

        if (
            openai_provider.available()
        ):
            ai_provider_registry.set_default(
                "openai"
            )

        elif (
            ai_provider_registry.get(
                "mock"
            )
        ):
            ai_provider_registry.set_default(
                "mock"
            )

        self._initialized = True

        return ai_provider_registry


ai_provider_bootstrap = (
    AIProviderBootstrap()
)
