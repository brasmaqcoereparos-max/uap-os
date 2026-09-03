from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceResponse:
    text: str

    speak: bool = True
    display: bool = True

    level: str = "info"

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "text": self.text,
            "speak": self.speak,
            "display": self.display,
            "level": self.level,
            "metadata": dict(
                self.metadata
            ),
        }
