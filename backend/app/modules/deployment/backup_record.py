from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class DeploymentBackupRecord:
    id: str

    source: str

    destination: str

    version: str = ""

    successful: bool = True

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

    def to_dict(self):
        return {
            "id": self.id,
            "source": self.source,
            "destination": (
                self.destination
            ),
            "version": self.version,
            "successful": (
                self.successful
            ),
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
