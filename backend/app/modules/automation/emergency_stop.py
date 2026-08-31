"""
Sistema de parada de emergência do UAP.
"""

from datetime import (
    datetime,
    timezone,
)


class EmergencyStop:

    def __init__(self):
        self.active = False

        self.reason = ""

        self.activated_at = None

    def activate(
        self,
        reason: str = (
            "Emergency stop"
        ),
    ):
        self.active = True

        self.reason = reason

        self.activated_at = (
            datetime.now(
                timezone.utc
            )
        )

        return True

    def release(self):
        self.active = False

        self.reason = ""

        self.activated_at = None

        return True

    def reset(self):
        return self.release()

    def is_active(self):
        return self.active

    def status(self):
        return {
            "active": (
                self.active
            ),
            "reason": (
                self.reason
            ),
            "activated_at": (
                self.activated_at.isoformat()
                if self.activated_at
                else None
            ),
        }


emergency_stop = (
    EmergencyStop()
        )
