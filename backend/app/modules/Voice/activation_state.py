from dataclasses import dataclass
from datetime import datetime
from datetime import timezone


@dataclass
class VoiceActivationState:
    active: bool = False

    activated_at: (
        datetime | None
    ) = None

    expires_at: (
        datetime | None
    ) = None

    def activate(
        self,
        expires_at: (
            datetime | None
        ) = None,
    ):
        self.active = True

        self.activated_at = (
            datetime.now(
                timezone.utc
            )
        )

        self.expires_at = (
            expires_at
        )

        return True

    def deactivate(self):
        self.active = False

        self.activated_at = None
        self.expires_at = None

        return True

    def to_dict(self):
        return {
            "active": self.active,
            "activated_at": (
                self.activated_at
                .isoformat()
                if self.activated_at
                else None
            ),
            "expires_at": (
                self.expires_at
                .isoformat()
                if self.expires_at
                else None
            ),
        }
