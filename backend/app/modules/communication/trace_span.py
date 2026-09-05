from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class CommunicationTraceSpan:
    id: str

    name: str

    trace_id: str

    parent_id: str | None = None

    started_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    finished_at: (
        datetime | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def finish(self):
        self.finished_at = (
            datetime.now(
                timezone.utc
            )
        )

        return self

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "trace_id": self.trace_id,
            "parent_id": (
                self.parent_id
            ),
            "started_at": (
                self.started_at
                .isoformat()
            ),
            "finished_at": (
                self.finished_at
                .isoformat()
                if self.finished_at
                else None
            ),
            "metadata": dict(
                self.metadata
            ),
      }
