"""
Conversation Manager - Manage multiple conversations in memory
"""

import logging
from typing import Dict, Optional, List
from .models import Conversation

logger = logging.getLogger(__name__)


class ConversationManager:
    """
    In-memory conversation manager
    For production, integrate with database layer
    """

    def __init__(self, max_conversations: int = 1000):
        self.conversations: Dict[str, Conversation] = {}
        self.max_conversations = max_conversations

    def create_conversation(
        self,
        user_id: Optional[str] = None,
        project_id: Optional[str] = None,
        title: str = "New Conversation",
    ) -> Conversation:
        """Create new conversation"""
        conversation = Conversation(
            user_id=user_id,
            project_id=project_id,
            title=title,
        )

        if len(self.conversations) >= self.max_conversations:
            # Remove oldest conversation
            oldest_id = min(
                self.conversations.keys(),
                key=lambda k: self.conversations[k].created_at
            )
            del self.conversations[oldest_id]
            logger.info(f"Removed oldest conversation {oldest_id}")

        self.conversations[conversation.id] = conversation
        logger.info(f"Created conversation {conversation.id}")
        return conversation

    def get_conversation(self, conversation_id: str) -> Optional[Conversation]:
        """Get conversation by ID"""
        return self.conversations.get(conversation_id)

    def update_conversation(self, conversation_id: str, conversation: Conversation) -> bool:
        """Update existing conversation"""
        if conversation_id not in self.conversations:
            return False
        self.conversations[conversation_id] = conversation
        return True

    def delete_conversation(self, conversation_id: str) -> bool:
        """Delete conversation"""
        if conversation_id not in self.conversations:
            return False
        del self.conversations[conversation_id]
        logger.info(f"Deleted conversation {conversation_id}")
        return True

    def list_conversations(
        self,
        user_id: Optional[str] = None,
        project_id: Optional[str] = None,
        limit: int = 50,
    ) -> List[Conversation]:
        """List conversations with optional filtering"""
        conversations = list(self.conversations.values())

        if user_id:
            conversations = [c for c in conversations if c.user_id == user_id]

        if project_id:
            conversations = [c for c in conversations if c.project_id == project_id]

        # Sort by updated_at descending
        conversations.sort(key=lambda c: c.updated_at, reverse=True)

        return conversations[:limit]

    def get_conversation_count(self) -> int:
        """Get total conversation count"""
        return len(self.conversations)

    def clear_all(self) -> None:
        """Clear all conversations"""
        self.conversations.clear()
        logger.info("Cleared all conversations")


# Global manager instance
conversation_manager = ConversationManager()
