from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.voice.enums import (
    VoiceIntentType,
)


@dataclass
class VoiceIntent:
    name: str

    intent_type: (
        VoiceIntentType
    ) = VoiceIntentType.UNKNOWN

    confidence: float = 0.0

    parameters: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    source_text: str = ""

    def to_dict(self):
        return {
            "name": self.name,
            "intent_type": (
                self.intent_type.value
            ),
            "confidence": (
                self.confidence
            ),
            "parameters": dict(
                self.parameters
            ),
            "source_text": (
                self.source_text
            ),
        }
