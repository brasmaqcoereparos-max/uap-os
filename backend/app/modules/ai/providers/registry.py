from __future__ import annotations

from typing import Any

from app.modules.ai.providers.base import (
    AIProvider,
)


class AIProviderRegistry:

    def __init__(self):
        self.providers: dict[
            str,
            AIProvider,
        ] = {}

        self.default_provider: (
            str | None
        ) = None

    def register(
        self,
        provider: AIProvider,
        default: bool = False,
    ):
        if not isinstance(
            provider,
            AIProvider,
        ):
            raise TypeError(
                "provider must be an "
                "AIProvider"
            )

        name = str(
            provider.name
        ).strip()

        if not name:
            raise ValueError(
                "AI provider name "
                "cannot be empty"
            )

        self.providers[
            name
        ] = provider

        if (
            default
            or self.default_provider
            is None
        ):
            self.default_provider = (
                name
            )

        return provider

    async def register_provider(
        self,
        provider: AIProvider,
        default: bool = False,
    ) -> bool:
        try:
            result = (
                await provider.initialize()
            )

            self.register(
                provider,
                default=default,
            )

            return bool(
                result
            )

        except Exception:
            self.register(
                provider,
                default=default,
            )

            return False

    def get(
        self,
        name: str | None = None,
    ):
        target = (
            name
            or self.default_provider
        )

        if not target:
            return None

        return self.providers.get(
            target
        )

    def get_provider(
        self,
        name: str | None = None,
    ):
        return self.get(
            name
        )

    def default(self):
        return self.get(
            self.default_provider
        )

    def set_default(
        self,
        name: str,
    ):
        if name not in self.providers:
            raise KeyError(
                "AI provider not found: "
                f"{name}"
            )

        self.default_provider = name

        return self.providers[
            name
        ]

    def list_all(self):
        return list(
            self.providers.values()
        )

    def list_providers(
        self,
    ) -> list[str]:
        return list(
            self.providers.keys()
        )

    def has_provider(
        self,
        name: str,
    ) -> bool:
        return (
            name
            in self.providers
        )

    def remove(
        self,
        name: str,
    ):
        provider = (
            self.providers.pop(
                name,
                None,
            )
        )

        if (
            provider is not None
            and self.default_provider
            == name
        ):
            self.default_provider = (
                next(
                    iter(
                        self.providers
                    ),
                    None,
                )
            )

        return provider

    async def get_health_all(
        self,
    ) -> dict[str, Any]:
        result = {}

        for (
            name,
            provider,
        ) in self.providers.items():
            try:
                result[
                    name
                ] = (
                    await provider
                    .health_check()
                )

            except Exception:
                result[
                    name
                ] = (
                    provider.get_health()
                )

        return result

    async def get_health(
        self,
        name: str | None = None,
    ):
        provider = self.get(
            name
        )

        if provider is None:
            return None

        try:
            return (
                await provider
                .health_check()
            )

        except Exception:
            return (
                provider.get_health()
            )

    async def initialize_default(
        self,
    ) -> bool:
        from app.modules.ai.providers.mock import (
            MockProvider,
        )

        provider = MockProvider()

        return (
            await self
            .register_provider(
                provider,
                default=True,
            )
        )

    async def shutdown_all(
        self,
    ) -> None:
        for provider in list(
            self.providers.values()
        ):
            try:
                await provider.shutdown()

            except Exception:
                pass

        self.clear()

    def clear(self):
        self.providers.clear()
        self.default_provider = None


ai_provider_registry = (
    AIProviderRegistry()
)

provider_registry = (
    ai_provider_registry
            )
