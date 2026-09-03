from app.modules.ai.enums import (
    AIMessageRole,
)
from app.modules.ai.message import (
    AIMessage,
)
from app.modules.ai.provider_manager import (
    ai_provider_manager,
)
from app.modules.ai.request import (
    AIRequest,
)


class AIService:

    def generate(
        self,
        request: AIRequest,
        provider_name: (
            str | None
        ) = None,
    ):
        provider = (
            ai_provider_manager.get(
                provider_name
            )
        )

        return provider.generate(
            request
        )

    def ask(
        self,
        text: str,
        system_prompt: (
            str | None
        ) = None,
        provider_name: (
            str | None
        ) = None,
        model: (
            str | None
        ) = None,
    ):
        request = AIRequest(
            model=model
        )

        if system_prompt:
            request.add_message(
                AIMessage(
                    role=(
                        AIMessageRole
                        .SYSTEM
                    ),
                    content=(
                        system_prompt
                    ),
                )
            )

        request.add_message(
            AIMessage(
                role=(
                    AIMessageRole.USER
                ),
                content=text,
            )
        )

        return self.generate(
            request=request,
            provider_name=(
                provider_name
            ),
        )

    def providers(self):
        return (
            ai_provider_manager
            .providers()
        )


ai_service = AIService()
