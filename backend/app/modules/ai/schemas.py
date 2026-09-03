"""
AI Schemas - Message, Request, Response structures
"""

from enum import Enum
from typing import Optional, Any, List, Dict
from datetime import datetime
from pydantic import BaseModel, Field


class MessageRole(str, Enum):
    """Message roles in conversation"""
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class AIMessage(BaseModel):
    """Single message in AI conversation"""
    role: MessageRole
    content: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class AIRequest(BaseModel):
    """Request to AI service"""
    conversation_id: Optional[str] = None
    project_id: Optional[str] = None
    user_id: Optional[str] = None
    message: str
    context: Optional[Dict[str, Any]] = None
    system_prompt: Optional[str] = None
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(default=2000, ge=100)
    include_reasoning: bool = False
    tool_use: bool = False

    class Config:
        json_schema_extra = {
            "example": {
                "message": "How do I create a smart home automation?",
                "project_id": "proj_123",
                "temperature": 0.7,
            }
        }


class AIResponse(BaseModel):
    """Response from AI service"""
    conversation_id: str
    message: str
    role: MessageRole = MessageRole.ASSISTANT
    thinking: Optional[str] = None
    intent: Optional[str] = None
    plan: Optional[List[str]] = None
    tools_used: Optional[List[str]] = None
    structured_output: Optional[Dict[str, Any]] = None
    safety_level: str = Field(default="safe")  # safe, requires_review, blocked
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ProviderStatus(str, Enum):
    """AI Provider status"""
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    ERROR = "error"
    INITIALIZING = "initializing"


class ProviderHealth(BaseModel):
    """Provider health check"""
    provider_name: str
    status: ProviderStatus
    available: bool
    error: Optional[str] = None
    last_check: datetime = Field(default_factory=datetime.utcnow)
    response_time_ms: Optional[float] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
