from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class VoiceFeedback:
    feedback_type: str

    message: str = ""

    tone: str | None = None

    vibration: bool = False

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "feedback_type": (
                self.feedback_type
            ),
            "message": self.message,
            "tone": self.tone,
            "vibration": (
                self.vibration
            ),
            "metadata": dict(
                self.metadata
            ),
        }
