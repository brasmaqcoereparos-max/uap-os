from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIResponse:
    text: str

    provider: str

    model: str | None = None

    success: bool = True

    error: str | None = None

    usage: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "text": self.text,
            "provider": self.provider,
            "model": self.model,
            "success": self.success,
            "error": self.error,
            "usage": dict(
                self.usage
            ),
            "metadata": dict(
                self.metadata
            ),
        }
