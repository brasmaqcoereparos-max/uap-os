from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceCommand:
    command: str

    parameters: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    source: str = "voice"

    confidence: float = 1.0

    requires_confirmation: (
        bool
    ) = False

    def to_dict(self):
        return {
            "command": self.command,
            "parameters": dict(
                self.parameters
            ),
            "source": self.source,
            "confidence": (
                self.confidence
            ),
            "requires_confirmation": (
                self.requires_confirmation
            ),
              }
