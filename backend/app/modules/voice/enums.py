from enum import Enum


class VoiceInputState(
    str,
    Enum,
):
    IDLE = "idle"
    LISTENING = "listening"
    PROCESSING = "processing"
    READY = "ready"
    ERROR = "error"


class VoiceIntentType(
    str,
    Enum,
):
    UNKNOWN = "unknown"

    COMMAND = "command"
    NAVIGATION = "navigation"
    QUERY = "query"
    CONTROL = "control"
    CONFIRMATION = "confirmation"
    CANCELLATION = "cancellation"
