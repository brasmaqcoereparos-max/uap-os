from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceTTSResult:
    provider: str

    text: str

    audio: bytes | None = None

    mime_type: str | None = None

    success: bool = True

    error: str | None = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "provider": self.provider,
            "text": self.text,
            "audio_size": (
                len(self.audio)
                if self.audio
                else 0
            ),
            "mime_type": (
                self.mime_type
            ),
            "success": self.success,
            "error": self.error,
            "metadata": dict(
                self.metadata
            ),
        }
