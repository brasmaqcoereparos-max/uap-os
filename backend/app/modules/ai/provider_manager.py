from __future__ import annotations

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
        registry: (
            AIProviderRegistry
        ) = ai_provider_registry,
    ):
        self.registry = registry

    def initialize(self):
        ai_provider_bootstrap.initialize()

        return self

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

        if provider is None:
            raise ValueError(
                "AI provider not found"
            )

        if not self._available(
            provider
        ):
            raise RuntimeError(
                "AI provider unavailable: "
                f"{provider.name}"
            )

        return provider

    def providers(self):
        self.initialize()

        default_provider = (
            self.registry.default()
        )

        return [
            {
                "name": provider.name,
                "available": (
                    self._available(
                        provider
                    )
                ),
                "default": (
                    provider
                    is default_provider
                ),
            }
            for provider
            in self.registry.list_all()
        ]

    def set_default(
        self,
        name: str,
    ):
        self.initialize()

        return (
            self.registry.set_default(
                name
            )
        )


ai_provider_manager = (
    AIProviderManager()
    )
