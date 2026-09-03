from app.modules.ai.provider_manager import (
    ai_provider_manager,
)
from app.modules.ai.schemas import (
    AIMessage,
    AIRequest,
    MessageRole,
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
        messages = []

        if system_prompt:
            messages.append(
                AIMessage(
                    role=(
                        MessageRole.SYSTEM
                    ),
                    content=(
                        system_prompt
                    ),
                )
            )

        messages.append(
            AIMessage(
                role=(
                    MessageRole.USER
                ),
                content=text,
            )
        )

        request = AIRequest(
            messages=messages,
            model=model,
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
