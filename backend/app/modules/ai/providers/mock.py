"""
Mock AI Provider - For testing without external API
"""

import asyncio
import time
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime
import random
import uuid

from .base import AIProvider
from ..schemas import AIMessage, AIResponse, MessageRole, ProviderHealth, ProviderStatus

logger = logging.getLogger(__name__)


class MockProvider(AIProvider):
    """
    Mock AI Provider - Simulates AI responses for testing
    No external dependencies or API keys required
    """

    def __init__(self, name: str = "mock", config: Optional[Dict[str, Any]] = None):
        super().__init__(name, config)
        self.response_delay = config.get("response_delay", 0.5) if config else 0.5
        self.responses = {
            "how": "I can help you with that! Let me provide a detailed explanation.",
            "create": "To create this, you'll need to follow these steps...",
            "explain": "Let me break this down for you:",
            "automate": "I can help you set up this automation. Here's what I suggest:",
            "hardware": "Based on your requirements, I recommend these components:",
            "suggest": "I have several suggestions for you:",
            "default": "That's an interesting question. Here's what I think:",
        }

    async def initialize(self) -> bool:
        """Initialize mock provider"""
        logger.info(f"Initializing Mock AI Provider: {self.name}")
        try:
            await asyncio.sleep(0.1)  # Simulate init time
            self.available = True
            self.last_check = datetime.utcnow()
            logger.info(f"Mock provider {self.name} initialized successfully")
            return True
        except Exception as e:
            self.last_error = str(e)
            logger.error(f"Failed to initialize mock provider: {e}")
            return False

    async def health_check(self) -> ProviderHealth:
        """Check mock provider health"""
        start = time.time()
        try:
            await asyncio.sleep(0.05)
            self.available = True
            self.last_error = None
            self.response_time_ms = (time.time() - start) * 1000
            return ProviderHealth(
                provider_name=self.name,
                status=ProviderStatus.AVAILABLE,
                available=True,
                response_time_ms=self.response_time_ms,
            )
        except Exception as e:
            self.available = False
            self.last_error = str(e)
            return ProviderHealth(
                provider_name=self.name,
                status=ProviderStatus.ERROR,
                available=False,
                error=self.last_error,
            )

    async def complete(
        self,
        messages: List[AIMessage],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> AIResponse:
        """Generate mock AI completion"""
        start = time.time()

        if not self.validate_message_list(messages):
            raise ValueError("Invalid message list")

        # Simulate response delay
        await asyncio.sleep(self.response_delay)

        # Extract user message (last message from user)
        user_message = None
        for msg in reversed(messages):
            if msg.role == MessageRole.USER:
                user_message = msg.content.lower()
                break

        if not user_message:
            user_message = ""

        # Select response based on keywords
        response_text = self._generate_response(user_message, max_tokens)

        # Generate mock structured output
        structured_output = self._generate_structured(user_message, kwargs.get("intent"))

        self.response_time_ms = (time.time() - start) * 1000

        return AIResponse(
            conversation_id=kwargs.get("conversation_id", str(uuid.uuid4())),
            message=response_text,
            role=MessageRole.ASSISTANT,
            thinking=f"Analyzing request: {user_message[:50]}...",
            intent=kwargs.get("intent", "help"),
            plan=self._generate_plan(user_message),
            tools_used=self._get_tools(user_message),
            structured_output=structured_output,
            safety_level="safe",
            confidence=0.95,
            timestamp=datetime.utcnow(),
        )

    def _generate_response(self, message: str, max_tokens: Optional[int]) -> str:
        """Generate response based on keywords"""
        base_response = None

        for keyword, response in self.responses.items():
            if keyword in message:
                base_response = response
                break

        if not base_response:
            base_response = self.responses["default"]

        # Add some context
        suffix = "\n\nWould you like me to provide more details or specific guidance?"
        response = base_response + suffix

        if max_tokens and len(response.split()) > max_tokens:
            words = response.split()[:max_tokens]
            response = " ".join(words) + "..."

        return response

    def _generate_plan(self, message: str) -> List[str]:
        """Generate mock plan steps"""
        plans = {
            "create": [
                "Define objectives",
                "Choose components",
                "Design circuit",
                "Test prototype",
                "Finalize design",
            ],
            "automate": [
                "Identify triggers",
                "Define actions",
                "Set conditions",
                "Test automation",
                "Deploy",
            ],
            "hardware": [
                "Analyze requirements",
                "Research options",
                "Compare specifications",
                "Select components",
                "Verify compatibility",
            ],
            "default": [
                "Gather information",
                "Analyze requirements",
                "Develop solution",
                "Test implementation",
                "Deploy and monitor",
            ],
        }

        for keyword, plan in plans.items():
            if keyword in message:
                return plan

        return plans["default"]

    def _get_tools(self, message: str) -> List[str]:
        """Get tools for this request"""
        tools = []

        if "automate" in message:
            tools.extend(["automation_builder", "rule_engine"])
        if "hardware" in message or "component" in message:
            tools.extend(["hardware_recommender", "compatibility_checker"])
        if "explain" in message or "how" in message:
            tools.extend(["knowledge_base"])
        if "design" in message or "plan" in message:
            tools.extend(["project_planner"])

        if not tools:
            tools.append("knowledge_base")

        return tools

    def _generate_structured(self, message: str, intent: Optional[str]) -> Dict[str, Any]:
        """Generate structured output"""
        return {
            "intent": intent or "help",
            "confidence": 0.95,
            "requires_hardware": "hardware" in message or "component" in message,
            "requires_code": "code" in message or "program" in message,
            "safety_concerns": False,
            "next_steps": self._generate_plan(message),
            "recommendations": self._get_recommendations(message),
        }

    def _get_recommendations(self, message: str) -> List[str]:
        """Get recommendations based on message"""
        recommendations = []

        if "beginner" in message or "learn" in message:
            recommendations.append("Start with simulator mode")
            recommendations.append("Use visual programming")

        if "advanced" in message or "professional" in message:
            recommendations.append("Use advanced settings")
            recommendations.append("Consider edge cases")

        if "hardware" in message:
            recommendations.append("Check compatibility matrix")
            recommendations.append("Review power requirements")

        if not recommendations:
            recommendations.append("Explore documentation")
            recommendations.append("Check examples")

        return recommendations
