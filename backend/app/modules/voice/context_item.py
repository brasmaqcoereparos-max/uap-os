from dataclasses import dataclass
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class VoiceContextItem:
    role: str
    content: str

    metadata: dict[
        str,
        Any,
    ]

    created_at: datetime

    @classmethod
    def create(
        cls,
        role: str,
        content: str,
        metadata: (
            dict[str, Any] | None
        ) = None,
    ):
        return cls(
            role=role,
            content=content,
            metadata=dict(
                metadata or {}
            ),
            created_at=datetime.now(
                timezone.utc
            ),
        )

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content,
            "metadata": dict(
                self.metadata
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
          }
