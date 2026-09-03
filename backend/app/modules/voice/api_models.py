from typing import Any

from pydantic import BaseModel
from pydantic import Field


class VoiceSessionCreateRequest(
    BaseModel
):
    language: str = "pt-BR"


class VoiceTextRequest(
    BaseModel
):
    text: str

    language: str = "pt-BR"

    confidence: (
        float | None
    ) = None

    session_id: (
        str | None
    ) = None


class VoiceStreamChunkRequest(
    BaseModel
):
    data: str

    sequence: int = 0
    final: bool = False

    sample_rate: int = 16000
    channels: int = 1
    sample_width: int = 2


class VoiceStreamProcessRequest(
    BaseModel
):
    session_id: (
        str | None
    ) = None

    language: str = "pt-BR"

    recognizer_name: (
        str | None
    ) = None


class VoiceCommandValidateRequest(
    BaseModel
):
    command: str

    parameters: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )

    source: str = "voice"

    confidence: float = 1.0

    requires_confirmation: (
        bool
    ) = False


class VoiceConfirmationRequest(
    BaseModel
):
    confirmation_id: str
