from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone


@dataclass
class SecurityLoginAttempt:
    principal_id: str

    success: bool

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    def to_dict(self):
        return {
            "principal_id": (
                self.principal_id
            ),
            "success": self.success,
            "created_at": (
                self.created_at
                .isoformat()
            ),
        }
