"""
AI Provider - Abstract base class
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from datetime import datetime
import logging

from ..schemas import AIMessage, AIResponse, ProviderStatus, ProviderHealth, MessageRole

logger = logging.getLogger(__name__)


class AIProvider(ABC):
    """Abstract base for AI providers"""

    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        self.name = name
        self.config = config or {}
        self.available = False
        self.last_error: Optional[str] = None
        self.last_check: Optional[datetime] = None
        self.response_time_ms: Optional[float] = None

    @abstractmethod
    async def initialize(self) -> bool:
        """Initialize provider connection/resources"""
        pass

    @abstractmethod
    async def health_check(self) -> ProviderHealth:
        """Check provider health"""
        pass

    @abstractmethod
    async def complete(
        self,
        messages: List[AIMessage],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> AIResponse:
        """Generate AI completion"""
        pass

    async def shutdown(self):
        """Cleanup resources"""
        self.available = False

    def get_health(self) -> ProviderHealth:
        """Get current provider health"""
        return ProviderHealth(
            provider_name=self.name,
            status=ProviderStatus.AVAILABLE if self.available else ProviderStatus.UNAVAILABLE,
            available=self.available,
            error=self.last_error,
            last_check=self.last_check or datetime.utcnow(),
            response_time_ms=self.response_time_ms,
        )

    @staticmethod
    def validate_message_list(messages: List[AIMessage]) -> bool:
        """Validate message list structure"""
        if not messages:
            return False
        if messages[0].role != MessageRole.SYSTEM and messages[0].role != MessageRole.USER:
            return False
        return True
