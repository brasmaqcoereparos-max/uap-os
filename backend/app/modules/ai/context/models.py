"""
Context Models - Data structures for conversation context
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
from enum import Enum


class UserLevel(str, Enum):
    """User experience level"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    PROFESSIONAL = "professional"


class Context:
    """Represents conversation context"""

    def __init__(self, conversation_id: str):
        self.conversation_id = conversation_id
        self.short_term: Dict[str, Any] = {}  # Recent messages, current topic
        self.project_context: Dict[str, Any] = {}  # Project info
        self.user_context: Dict[str, Any] = {}  # User preferences
        self.intent_context: Dict[str, Any] = {}  # Detected intent
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def set_project_info(self, project_id: str, project_data: Dict[str, Any]) -> None:
        """Set project context"""
        self.project_context = {
            "project_id": project_id,
            "data": project_data,
            "updated_at": datetime.utcnow().isoformat(),
        }
        self.updated_at = datetime.utcnow()

    def set_user_level(self, level: UserLevel) -> None:
        """Set user experience level"""
        self.user_context["level"] = level.value
        self.updated_at = datetime.utcnow()

    def set_intent(self, intent: str, confidence: float = 1.0) -> None:
        """Set detected intent"""
        self.intent_context = {
            "intent": intent,
            "confidence": confidence,
            "detected_at": datetime.utcnow().isoformat(),
        }
        self.updated_at = datetime.utcnow()

    def update_short_term(self, key: str, value: Any) -> None:
        """Update short-term context"""
        self.short_term[key] = value
        self.updated_at = datetime.utcnow()

    def get_short_term(self, key: str, default: Any = None) -> Any:
        """Get short-term context value"""
        return self.short_term.get(key, default)

    def clear_short_term(self) -> None:
        """Clear short-term context"""
        self.short_term.clear()
        self.updated_at = datetime.utcnow()

    def get_all(self) -> Dict[str, Any]:
        """Get all context"""
        return {
            "conversation_id": self.conversation_id,
            "short_term": self.short_term,
            "project": self.project_context,
            "user": self.user_context,
            "intent": self.intent_context,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return self.get_all()
