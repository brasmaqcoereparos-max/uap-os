from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel
from pydantic import Field


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class AIMessage(BaseModel):
    role: MessageRole
    content: str

    timestamp: datetime = Field(
        default_factory=datetime.utcnow
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class AIRequest(BaseModel):
    conversation_id: str | None = None
    project_id: str | None = None
    user_id: str | None = None

    message: str | None = None

    messages: list[AIMessage] = Field(
        default_factory=list
    )

    context: dict[str, Any] | None = None

    system_prompt: str | None = None

    model: str | None = None

    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
    )

    max_tokens: int | None = Field(
        default=2000,
        ge=1,
    )

    max_output_tokens: int | None = Field(
        default=None,
        ge=1,
    )

    include_reasoning: bool = False
    tool_use: bool = False

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

    def normalized_messages(
        self,
    ) -> list[AIMessage]:
        result = list(
            self.messages
        )

        if (
            self.system_prompt
            and not any(
                message.role
                == MessageRole.SYSTEM
                for message in result
            )
        ):
            result.insert(
                0,
                AIMessage(
                    role=MessageRole.SYSTEM,
                    content=self.system_prompt,
                ),
            )

        if (
            self.message
            and not any(
                message.role
                == MessageRole.USER
                and message.content
                == self.message
                for message in result
            )
        ):
            result.append(
                AIMessage(
                    role=MessageRole.USER,
                    content=self.message,
                )
            )

        return result


class AIResponse(BaseModel):
    conversation_id: str | None = None

    message: str = ""
    text: str = ""

    role: MessageRole = (
        MessageRole.ASSISTANT
    )

    provider: str | None = None
    model: str | None = None

    success: bool = True
    error: str | None = None

    thinking: str | None = None
    intent: str | None = None

    plan: list[str] | None = None
    tools_used: list[str] | None = None

    structured_output: (
        dict[str, Any] | None
    ) = None

    safety_level: str = "safe"

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )

    usage: dict[str, Any] = Field(
        default_factory=dict
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )

    timestamp: datetime = Field(
        default_factory=datetime.utcnow
    )

    def model_post_init(
        self,
        __context: Any,
    ) -> None:
        if self.text and not self.message:
            self.message = self.text

        elif self.message and not self.text:
            self.text = self.message


class ProviderStatus(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    ERROR = "error"
    INITIALIZING = "initializing"


class ProviderHealth(BaseModel):
    provider_name: str

    status: ProviderStatus

    available: bool

    error: str | None = None

    last_check: datetime = Field(
        default_factory=datetime.utcnow
    )

    response_time_ms: (
        float | None
    ) = None

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )
