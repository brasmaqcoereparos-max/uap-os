from enum import Enum


class AIMessageRole(
    str,
    Enum,
):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class AIProviderState(
    str,
    Enum,
):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    DISABLED = "disabled"
    ERROR = "error"
