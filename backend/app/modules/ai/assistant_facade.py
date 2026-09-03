from app.modules.ai.assistant_service import (
    ai_assistant_service,
)
from app.modules.ai.session_service import (
    ai_session_service,
)


class AIAssistantFacade:

    def create_session(
        self,
        user_id: (
            str | None
        ) = None,
        project_id: (
            str | None
        ) = None,
        user_level: (
            str | None
        ) = None,
    ):
        return (
            ai_session_service
            .create_session(
                user_id=user_id,
                project_id=project_id,
                user_level=user_level,
            )
        )

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
        return (
            ai_assistant_service
            .ask(
                session_id=session_id,
                text=text,
                provider_name=(
                    provider_name
                ),
                model=model,
            )
        )


ai_assistant_facade = (
    AIAssistantFacade()
)
