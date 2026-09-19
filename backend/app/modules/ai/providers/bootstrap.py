from __future__ import annotations

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

    @staticmethod
    def _available(
        provider,
    ) -> bool:
        available = getattr(
            provider,
            "available",
            False,
        )

        if callable(
            available
        ):
            try:
                return bool(
                    available()
                )

            except Exception:
                return False

        return bool(
            available
        )

    def initialize(self):
        if self._initialized:
            return (
                ai_provider_registry
            )

        if (
            ai_provider_registry.get(
                "mock"
            )
            is None
        ):
            ai_provider_registry.register(
                MockProvider(),
                default=True,
            )

        if (
            ai_provider_registry.get(
                "openai"
            )
            is None
        ):
            ai_provider_registry.register(
                openai_provider
            )

        if self._available(
            openai_provider
        ):
            ai_provider_registry.set_default(
                "openai"
            )

        else:
            ai_provider_registry.set_default(
                "mock"
            )

        self._initialized = True

        return (
            ai_provider_registry
        )

    def reset(self):
        self._initialized = False

        ai_provider_registry.clear()

        return self.initialize()


ai_provider_bootstrap = (
    AIProviderBootstrap()
        )
