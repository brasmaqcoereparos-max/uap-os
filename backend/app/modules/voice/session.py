import uuid
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any

from app.modules.voice.enums import (
    VoiceInputState,
)


@dataclass
class VoiceSession:
    id: str = field(
        default_factory=lambda: (
            str(uuid.uuid4())
        )
    )

    language: str = "pt-BR"

    state: VoiceInputState = (
        VoiceInputState.IDLE
    )

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def set_state(
        self,
        state: VoiceInputState,
    ):
        self.state = state

        return state

    def to_dict(self):
        return {
            "id": self.id,
            "language": self.language,
            "state": self.state.value,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
  }
