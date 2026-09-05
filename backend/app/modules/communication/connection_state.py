from enum import Enum


class CommunicationConnectionState(
    str,
    Enum,
):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    DEGRADED = "degraded"
    ERROR = "error"
