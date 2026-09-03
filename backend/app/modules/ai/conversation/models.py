"""
Conversation Models - Data structures for conversations
"""

from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid

from ..schemas import AIMessage, MessageRole


class Conversation:
    """Represents an AI conversation session"""

    def __init__(
        self,
        conversation_id: Optional[str] = None,
        user_id: Optional[str] = None,
        project_id: Optional[str] = None,
        title: str = "New Conversation",
    ):
        self.id = conversation_id or str(uuid.uuid4())
        self.user_id = user_id
        self.project_id = project_id
        self.title = title
        self.messages: List[AIMessage] = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.metadata: Dict[str, Any] = {}
        self.token_count = 0

    def add_message(self, message: AIMessage) -> None:
        """Add message to conversation"""
        self.messages.append(message)
        self.updated_at = datetime.utcnow()
        # Rough token estimation (words * 1.3)
        self.token_count += int(len(message.content.split()) * 1.3)

    def add_user_message(self, content: str) -> AIMessage:
        """Add user message and return it"""
        msg = AIMessage(role=MessageRole.USER, content=content)
        self.add_message(msg)
        return msg

    def add_assistant_message(self, content: str) -> AIMessage:
        """Add assistant message and return it"""
        msg = AIMessage(role=MessageRole.ASSISTANT, content=content)
        self.add_message(msg)
        return msg

    def add_system_message(self, content: str) -> AIMessage:
        """Add system message and return it"""
        msg = AIMessage(role=MessageRole.SYSTEM, content=content)
        self.add_message(msg)
        return msg

    def get_messages(self, limit: Optional[int] = None) -> List[AIMessage]:
        """Get messages with optional limit (most recent)"""
        messages = self.messages
        if limit and len(messages) > limit:
            messages = messages[-limit:]
        return messages

    def get_last_user_message(self) -> Optional[AIMessage]:
        """Get last user message"""
        for msg in reversed(self.messages):
            if msg.role == MessageRole.USER:
                return msg
        return None

    def clear_messages(self) -> None:
        """Clear all messages"""
        self.messages.clear()
        self.token_count = 0
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "project_id": self.project_id,
            "title": self.title,
            "message_count": len(self.messages),
            "token_count": self.token_count,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "metadata": self.metadata,
        }
