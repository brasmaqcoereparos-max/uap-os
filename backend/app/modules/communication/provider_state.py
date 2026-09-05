from enum import Enum


class CommunicationProviderState(
    str,
    Enum,
):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    DISABLED = "disabled"
    ERROR = "error"
