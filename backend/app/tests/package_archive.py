from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone


@dataclass
class DeploymentPackageArchive:
    path: str

    format: str

    size: int = 0

    checksum: str = ""

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def to_dict(self):
        return {
            "path": self.path,
            "format": self.format,
            "size": self.size,
            "checksum": self.checksum,
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
