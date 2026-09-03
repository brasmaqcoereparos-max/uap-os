from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ai.message import (
    AIMessage,
)


@dataclass
class AIRequest:
    messages: list[
        AIMessage
    ] = field(
        default_factory=list
    )

    model: str | None = None

    temperature: float | None = None

    max_output_tokens: (
        int | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_message(
        self,
        message: AIMessage,
    ):
        self.messages.append(
            message
        )

        return message

    def to_dict(self):
        return {
            "messages": [
                message.to_dict()
                for message
                in self.messages
            ],
            "model": self.model,
            "temperature": (
                self.temperature
            ),
            "max_output_tokens": (
                self.max_output_tokens
            ),
            "metadata": dict(
                self.metadata
            ),
              }
