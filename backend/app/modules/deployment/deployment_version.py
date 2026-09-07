from dataclasses import dataclass
from datetime import datetime
from datetime import timezone


@dataclass
class DeploymentVersion:
    version: str

    build: str = ""

    created_at: datetime = (
        datetime.now(
            timezone.utc
        )
    )

    def to_dict(self):
        return {
            "version": self.version,
            "build": self.build,
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
