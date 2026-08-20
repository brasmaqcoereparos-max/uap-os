from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class UAPMessage:
    message_type: str
    payload: dict[str, Any] = field(
        default_factory=dict
    )
    message_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "message_id": self.message_id,
            "message_type": self.message_type,
            "payload": self.payload,
            "timestamp": self.timestamp.isoformat(),
        }

    def encode(self) -> bytes:
        return (
            json.dumps(
                self.to_dict(),
                ensure_ascii=False,
            ).encode("utf-8")
        )

    @classmethod
    def decode(
        cls,
        data: bytes | str,
    ) -> "UAPMessage":
        if isinstance(data, bytes):
            data = data.decode("utf-8")

        raw = json.loads(data)

        timestamp = datetime.fromisoformat(
            raw["timestamp"]
        )

        return cls(
            message_type=raw["message_type"],
            payload=raw.get("payload", {}),
            message_id=raw["message_id"],
            timestamp=timestamp,
        )
