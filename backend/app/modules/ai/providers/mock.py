from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from app.modules.ai.providers.base import (
    AIProvider,
)
from app.modules.ai.schemas import (
    AIRequest,
    AIResponse,
    MessageRole,
    ProviderHealth,
    ProviderStatus,
)


class MockProvider(
    AIProvider
):

    def __init__(
        self,
        name: str = "mock",
        config: (
            dict[str, Any] | None
        ) = None,
    ):
        super().__init__(
            name=name,
            config=config,
        )

        self._available = True

    def available(self) -> bool:
        return True

    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        messages = (
            request.normalized_messages()
        )

        user_text = ""

        for message in reversed(
            messages
        ):
            if (
                message.role
                == MessageRole.USER
            ):
                user_text = (
                    message.content
                )

                break

        response_text = (
            self._generate_response(
                user_text
            )
        )

        return AIResponse(
            conversation_id=(
                request.conversation_id
                or str(
                    uuid.uuid4()
                )
            ),
            message=response_text,
            text=response_text,
            provider=self.name,
            model=(
                request.model
                or "mock"
            ),
            success=True,
            intent=self._intent(
                user_text
            ),
            plan=self._plan(
                user_text
            ),
            structured_output={
                "intent": (
                    self._intent(
                        user_text
                    )
                ),
                "next_steps": (
                    self._plan(
                        user_text
                    )
                ),
                "simulation": True,
            },
            safety_level="safe",
            confidence=0.95,
            metadata={
                "mock": True,
            },
        )

    def _generate_response(
        self,
        text: str,
    ) -> str:
        lowered = str(
            text
        ).lower()

        if any(
            word in lowered
            for word in (
                "criar",
                "create",
                "projeto",
                "project",
            )
        ):
            return (
                "Posso ajudar a estruturar "
                "esse projeto passo a passo."
            )

        if any(
            word in lowered
            for word in (
                "hardware",
                "placa",
                "sensor",
                "motor",
            )
        ):
            return (
                "Vou analisar os requisitos "
                "de hardware e compatibilidade."
            )

        if any(
            word in lowered
            for word in (
                "automat",
                "sequência",
                "fluxo",
            )
        ):
            return (
                "Vou organizar a automação "
                "em etapas verificáveis."
            )

        return (
            "Posso ajudar com o projeto "
            "UAP."
        )

    def _intent(
        self,
        text: str,
    ) -> str:
        lowered = str(
            text
        ).lower()

        if "hardware" in lowered:
            return "hardware"

        if (
            "automat"
            in lowered
        ):
            return "automation"

        if (
            "projeto"
            in lowered
            or "project"
            in lowered
        ):
            return "project"

        return "help"

    def _plan(
        self,
        text: str,
    ) -> list[str]:
        return [
            "Analisar solicitação",
            "Validar requisitos",
            "Gerar proposta",
            "Validar segurança",
            "Solicitar aprovação "
            "quando necessário",
        ]

    async def initialize(
        self,
    ) -> bool:
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

        return ProviderHealth(
            provider_name=self.name,
            status=(
                ProviderStatus.AVAILABLE
            ),
            available=True,
            last_check=self.last_check,
    )
