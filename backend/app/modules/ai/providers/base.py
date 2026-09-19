from __future__ import annotations

from datetime import datetime
from typing import Any

from app.modules.ai.schemas import (
    AIRequest,
    AIResponse,
    ProviderHealth,
    ProviderStatus,
)


class AIProvider:

    def __init__(
        self,
        name: str | None = None,
        config: (
            dict[str, Any] | None
        ) = None,
    ):
        self._provider_name = (
            name
            or self.__class__.__name__
            .lower()
        )

        self.config = dict(
            config or {}
        )

        self.last_error: (
            str | None
        ) = None

        self.last_check: (
            datetime | None
        ) = None

        self.response_time_ms: (
            float | None
        ) = None

        self._available = False

    @property
    def name(self) -> str:
        return self._provider_name

    def available(self) -> bool:
        return bool(
            self._available
        )

    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        raise NotImplementedError(
            f"Provider '{self.name}' "
            "does not implement generate()"
        )

    async def initialize(self) -> bool:
        self._available = True
        self.last_error = None
        self.last_check = (
            datetime.utcnow()
        )

        return True

    async def health_check(
        self,
    ) -> ProviderHealth:
        self.last_check = (
            datetime.utcnow()
        )

        return self.get_health()

    async def complete(
        self,
        messages,
        temperature: float = 0.7,
        max_tokens: int | None = None,
        **kwargs,
    ) -> AIResponse:
        request = AIRequest(
            messages=list(
                messages or []
            ),
            temperature=temperature,
            max_tokens=max_tokens,
            model=kwargs.get(
                "model"
            ),
            conversation_id=(
                kwargs.get(
                    "conversation_id"
                )
            ),
            metadata={
                key: value
                for key, value
                in kwargs.items()
                if key not in {
                    "model",
                    "conversation_id",
                }
            },
        )

        return self.generate(
            request
        )

    async def shutdown(self):
        self._available = False

    def get_health(
        self,
    ) -> ProviderHealth:
        available = self.available()

        if self.last_error:
            status = (
                ProviderStatus.ERROR
            )

        elif available:
            status = (
                ProviderStatus.AVAILABLE
            )

        else:
            status = (
                ProviderStatus.UNAVAILABLE
            )

        return ProviderHealth(
            provider_name=self.name,
            status=status,
            available=available,
            error=self.last_error,
            last_check=(
                self.last_check
                or datetime.utcnow()
            ),
            response_time_ms=(
                self.response_time_ms
            ),
        )

    @staticmethod
    def validate_message_list(
        messages,
    ) -> bool:
        if not messages:
            return False

        for message in messages:
            if not hasattr(
                message,
                "role",
            ):
                return False

            if not hasattr(
                message,
                "content",
            ):
                return False

        return True
