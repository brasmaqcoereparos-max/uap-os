"""
Context Manager - Manage conversation contexts
"""

import logging
from typing import Dict, Optional
from .models import Context, UserLevel

logger = logging.getLogger(__name__)


class ContextManager:
    """
    Manager for conversation contexts
    Handles short-term, project, and user contexts
    """

    def __init__(self, max_contexts: int = 1000):
        self.contexts: Dict[str, Context] = {}
        self.max_contexts = max_contexts

    def create_context(self, conversation_id: str) -> Context:
        """Create new context"""
        if conversation_id in self.contexts:
            logger.warning(f"Context {conversation_id} already exists")
            return self.contexts[conversation_id]

        context = Context(conversation_id)
        self.contexts[conversation_id] = context
        logger.debug(f"Created context for {conversation_id}")
        return context

    def get_context(self, conversation_id: str) -> Optional[Context]:
        """Get context"""
        return self.contexts.get(conversation_id)

    def get_or_create_context(self, conversation_id: str) -> Context:
        """Get existing or create new context"""
        context = self.get_context(conversation_id)
        if context is None:
            context = self.create_context(conversation_id)
        return context

    def set_project_context(
        self,
        conversation_id: str,
        project_id: str,
        project_data: Optional[Dict] = None,
    ) -> bool:
        """Set project context"""
        context = self.get_or_create_context(conversation_id)
        context.set_project_info(project_id, project_data or {})
        return True

    def set_user_level(
        self,
        conversation_id: str,
        level: UserLevel,
    ) -> bool:
        """Set user experience level"""
        context = self.get_or_create_context(conversation_id)
        context.set_user_level(level)
        return True

    def set_intent(
        self,
        conversation_id: str,
        intent: str,
        confidence: float = 1.0,
    ) -> bool:
        """Set detected intent"""
        context = self.get_or_create_context(conversation_id)
        context.set_intent(intent, confidence)
        return True

    def delete_context(self, conversation_id: str) -> bool:
        """Delete context"""
        if conversation_id not in self.contexts:
            return False
        del self.contexts[conversation_id]
        logger.debug(f"Deleted context {conversation_id}")
        return True

    def clear_short_term(self, conversation_id: str) -> bool:
        """Clear short-term context"""
        context = self.get_context(conversation_id)
        if context is None:
            return False
        context.clear_short_term()
        return True

    def trim_contexts(self, max_token_count: int = 4000) -> None:
        """
        Trim old contexts when memory exceeds limit
        Keeps recent messages within max_token_count
        """
        # For now, just limit stored contexts
        if len(self.contexts) > self.max_contexts:
            # Remove oldest contexts
            sorted_contexts = sorted(
                self.contexts.items(),
                key=lambda x: x[1].created_at
            )
            to_remove = len(sorted_contexts) - self.max_contexts
            for conv_id, _ in sorted_contexts[:to_remove]:
                del self.contexts[conv_id]
            logger.info(f"Trimmed {to_remove} contexts")

    def clear_all(self) -> None:
        """Clear all contexts"""
        self.contexts.clear()
        logger.info("Cleared all contexts")


# Global manager instance
context_manager = ContextManager()
