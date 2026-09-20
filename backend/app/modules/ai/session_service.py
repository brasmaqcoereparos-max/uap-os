from __future__ import annotations

import uuid
from typing import Any

from app.modules.ai.context.manager import (
    ContextManager,
)
from app.modules.ai.context.models import (
    UserLevel,
)
from app.modules.ai.conversation.manager import (
    ConversationManager,
)
from app.modules.ai.schemas import (
    AIMessage,
    MessageRole,
)


class AISessionService:

    VALID_USER_LEVELS = {
        "beginner",
        "intermediate",
        "professional",
    }

    def __init__(self):
        self.context_manager = (
            ContextManager()
        )

        self.conversation_manager = (
            ConversationManager()
        )

        self._conversation_ids: dict[
            str,
            str,
        ] = {}

    def _normalize_user_level(
        self,
        user_level: str | None,
    ) -> str:
        if user_level is None:
            return "beginner"

        normalized = str(
            user_level
        ).strip().lower()

        if (
            normalized
            not in self.VALID_USER_LEVELS
        ):
            raise ValueError(
                "Unsupported AI user level: "
                f"{user_level}"
            )

        return normalized

    def create_session(
        self,
        user_id: str | None = None,
        project_id: str | None = None,
        user_level: str | None = None,
    ):
        session_id = str(
            uuid.uuid4()
        )

        level = (
            self._normalize_user_level(
                user_level
            )
        )

        context = (
            self.context_manager
            .create_context(
                session_id
            )
        )

        self.context_manager.set_user_level(
            session_id,
            UserLevel(
                level
            ),
        )

        if project_id:
            self.context_manager.set_project_context(
                conversation_id=(
                    session_id
                ),
                project_id=(
                    project_id
                ),
                project_data={},
            )

        context.user_context[
            "user_id"
        ] = user_id

        context.user_context[
            "level"
        ] = level

        conversation = (
            self.conversation_manager
            .create_conversation(
                user_id=user_id,
                project_id=project_id,
                title=(
                    "UAP AI Session"
                ),
            )
        )

        self._conversation_ids[
            session_id
        ] = conversation.id

        return {
            "session_id": session_id,
            "context": context,
            "conversation": (
                conversation
            ),
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
        conversation_id = (
            self._conversation_ids.get(
                session_id
            )
        )

        if conversation_id is None:
            return None

        return (
            self.conversation_manager
            .get_conversation(
                conversation_id
            )
        )

    def require_context(
        self,
        session_id: str,
    ):
        context = self.get_context(
            session_id
        )

        if context is None:
            raise ValueError(
                "AI session context "
                "not found"
            )

        return context

    def require_conversation(
        self,
        session_id: str,
    ):
        conversation = (
            self.get_conversation(
                session_id
            )
        )

        if conversation is None:
            raise ValueError(
                "AI conversation "
                "not found"
            )

        return conversation

    def set_user_level(
        self,
        session_id: str,
        level: str,
    ) -> str:
        normalized = (
            self._normalize_user_level(
                level
            )
        )

        self.require_context(
            session_id
        )

        self.context_manager.set_user_level(
            session_id,
            UserLevel(
                normalized
            ),
        )

        context = (
            self.require_context(
                session_id
            )
        )

        context.user_context[
            "level"
        ] = normalized

        return normalized

    def get_user_level(
        self,
        session_id: str,
    ) -> str:
        context = (
            self.require_context(
                session_id
            )
        )

        return str(
            context.user_context.get(
                "level",
                "beginner",
            )
        )

    def set_project_context(
        self,
        session_id: str,
        project_id: str,
        project_data: (
            dict[str, Any] | None
        ) = None,
    ) -> bool:
        self.require_context(
            session_id
        )

        result = (
            self.context_manager
            .set_project_context(
                conversation_id=(
                    session_id
                ),
                project_id=(
                    project_id
                ),
                project_data=(
                    project_data or {}
                ),
            )
        )

        conversation = (
            self.get_conversation(
                session_id
            )
        )

        if conversation is not None:
            conversation.project_id = (
                project_id
            )

        return result

    def set_intent(
        self,
        session_id: str,
        intent: str,
        confidence: float = 1.0,
    ) -> bool:
        self.require_context(
            session_id
        )

        return (
            self.context_manager
            .set_intent(
                conversation_id=(
                    session_id
                ),
                intent=intent,
                confidence=confidence,
            )
        )

    def update_context(
        self,
        session_id: str,
        key: str,
        value: Any,
    ) -> Any:
        context = (
            self.require_context(
                session_id
            )
        )

        context.update_short_term(
            key,
            value,
        )

        return value

    def add_user_message(
        self,
        session_id: str,
        text: str,
    ):
        conversation = (
            self.require_conversation(
                session_id
            )
        )

        normalized = str(
            text
        ).strip()

        if not normalized:
            raise ValueError(
                "AI user message "
                "cannot be empty"
            )

        message = AIMessage(
            role=MessageRole.USER,
            content=normalized,
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
            self.require_conversation(
                session_id
            )
        )

        normalized = str(
            text
        ).strip()

        if not normalized:
            raise ValueError(
                "AI assistant message "
                "cannot be empty"
            )

        message = AIMessage(
            role=(
                MessageRole.ASSISTANT
            ),
            content=normalized,
        )

        conversation.add_message(
            message
        )

        return message

    def messages(
        self,
        session_id: str,
        limit: int | None = None,
    ):
        conversation = (
            self.require_conversation(
                session_id
            )
        )

        return conversation.get_messages(
            limit=limit
        )

    def snapshot(
        self,
        session_id: str,
    ) -> dict[str, Any]:
        context = (
            self.require_context(
                session_id
            )
        )

        conversation = (
            self.require_conversation(
                session_id
            )
        )

        return {
            "session_id": session_id,
            "user_level": (
                self.get_user_level(
                    session_id
                )
            ),
            "context": (
                context.to_dict()
            ),
            "conversation": (
                conversation.to_dict()
            ),
            "messages": [
                (
                    message.model_dump()
                    if hasattr(
                        message,
                        "model_dump",
                    )
                    else {
                        "role": (
                            message.role
                        ),
                        "content": (
                            message.content
                        ),
                    }
                )
                for message
                in conversation.messages
            ],
        }

    def delete_session(
        self,
        session_id: str,
    ) -> bool:
        context_removed = (
            self.context_manager
            .delete_context(
                session_id
            )
        )

        conversation_id = (
            self._conversation_ids.pop(
                session_id,
                None,
            )
        )

        conversation_removed = False

        if conversation_id:
            conversation_removed = (
                self.conversation_manager
                .delete_conversation(
                    conversation_id
                )
            )

        return (
            context_removed
            or conversation_removed
        )


ai_session_service = (
    AISessionService()
                   )
