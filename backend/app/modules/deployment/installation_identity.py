from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class InstallationIdentity:
    installation_id: str

    target: str

    hostname: str

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
            "installation_id": (
                self.installation_id
            ),
            "target": self.target,
            "hostname": self.hostname,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
