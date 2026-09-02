from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceTranscript:
    text: str

    language: str = "pt-BR"

    confidence: float | None = None

    final: bool = True

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def normalized_text(self):
        return " ".join(
            self.text
            .strip()
            .split()
        )

    def is_empty(self):
        return not bool(
            self.normalized_text()
        )

    def to_dict(self):
        return {
            "text": self.text,
            "language": self.language,
            "confidence": (
                self.confidence
            ),
            "final": self.final,
            "metadata": dict(
                self.metadata
            ),
        }
