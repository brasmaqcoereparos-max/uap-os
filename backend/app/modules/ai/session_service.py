import uuid

from app.modules.ai.context.manager import (
    ContextManager,
)
from app.modules.ai.conversation.manager import (
    ConversationManager,
)
from app.modules.ai.schemas import (
    AIMessage,
    MessageRole,
)


class AISessionService:

    def __init__(self):
        self.context_manager = (
            ContextManager()
        )

        self.conversation_manager = (
            ConversationManager()
        )

    def create_session(
        self,
        user_id: str | None = None,
        project_id: str | None = None,
        user_level: str | None = None,
    ):
        session_id = str(
            uuid.uuid4()
        )

        context = (
            self.context_manager
            .create_context(
                session_id=session_id,
                user_id=user_id,
                project_id=project_id,
                user_level=user_level,
            )
        )

        conversation = (
            self.conversation_manager
            .create_conversation(
                session_id=session_id,
            )
        )

        return {
            "session_id": session_id,
            "context": context,
            "conversation": conversation,
        }

    def get_context(
        self,
        session_id: str,
    ):
        return (
            self.context_manager
            .get_context(
                session_id
            )
        )

    def get_conversation(
        self,
        session_id: str,
    ):
        return (
            self.conversation_manager
            .get_conversation(
                session_id
            )
        )

    def add_user_message(
        self,
        session_id: str,
        text: str,
    ):
        conversation = (
            self.get_conversation(
                session_id
            )
        )

        if not conversation:
            raise ValueError(
                "AI conversation not found"
            )

        message = AIMessage(
            role=MessageRole.USER,
            content=text,
        )

        conversation.add_message(
            message
        )

        return message

    def add_assistant_message(
        self,
        session_id: str,
        text: str,
    ):
        conversation = (
            self.get_conversation(
                session_id
            )
        )

        if not conversation:
            raise ValueError(
                "AI conversation not found"
            )

        message = AIMessage(
            role=MessageRole.ASSISTANT,
            content=text,
        )

        conversation.add_message(
            message
        )

        return message


ai_session_service = (
    AISessionService()
      )
