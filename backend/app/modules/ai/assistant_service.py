from app.modules.ai.context_prompt import (
    ai_context_prompt,
)
from app.modules.ai.schemas import (
    AIMessage,
    AIRequest,
    MessageRole,
)
from app.modules.ai.service import (
    ai_service,
)
from app.modules.ai.session_service import (
    ai_session_service,
)


class AIAssistantService:

    def ask(
        self,
        session_id: str,
        text: str,
        provider_name: (
            str | None
        ) = None,
        model: (
            str | None
        ) = None,
    ):
        context = (
            ai_session_service
            .get_context(
                session_id
            )
        )

        conversation = (
            ai_session_service
            .get_conversation(
                session_id
            )
        )

        if not conversation:
            raise ValueError(
                "AI conversation not found"
            )

        ai_session_service
        .add_user_message(
            session_id,
            text,
        )

        request = AIRequest(
            model=model
        )

        context_text = (
            ai_context_prompt.build(
                context
            )
        )

        if context_text:
            request.messages.append(
                AIMessage(
                    role=(
                        MessageRole.SYSTEM
                    ),
                    content=(
                        context_text
                    ),
                )
            )

        for message in (
            conversation.messages
        ):
            request.messages.append(
                message
            )

        response = (
            ai_service.generate(
                request=request,
                provider_name=(
                    provider_name
                ),
            )
        )

        if response.success:
            ai_session_service
            .add_assistant_message(
                session_id,
                response.text,
            )

        return response


ai_assistant_service = (
    AIAssistantService()
      )
