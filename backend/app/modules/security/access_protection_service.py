from app.modules.security.lockout_manager import (
    security_lockout_manager,
)
from app.modules.security.rate_limiter import (
    security_rate_limiter,
)
from app.modules.security.security_event import (
    SecurityEvent,
)
from app.modules.security.security_event_log import (
    security_event_log,
)


class SecurityAccessProtectionService:

    def check(
        self,
        principal_id: str,
        rate_key: str | None = None,
    ):
        if (
            security_lockout_manager
            .is_locked(
                principal_id
            )
        ):
            security_event_log.add(
                SecurityEvent(
                    event_type=(
                        "access_locked"
                    ),
                    source=(
                        principal_id
                    ),
                    severity="warning",
                )
            )

            return {
                "allowed": False,
                "reason": "locked",
            }

        key = (
            rate_key
            or principal_id
        )

        if not (
            security_rate_limiter
            .allow(key)
        ):
            security_event_log.add(
                SecurityEvent(
                    event_type=(
                        "rate_limit_exceeded"
                    ),
                    source=(
                        principal_id
                    ),
                    severity="warning",
                )
            )

            return {
                "allowed": False,
                "reason": (
                    "rate_limited"
                ),
            }

        return {
            "allowed": True,
            "reason": None,
        }

    def record_login(
        self,
        principal_id: str,
        success: bool,
    ):
        if success:
            security_lockout_manager.clear(
                principal_id
            )

            security_event_log.add(
                SecurityEvent(
                    event_type=(
                        "login_success"
                    ),
                    source=(
                        principal_id
                    ),
                    severity="info",
                )
            )

            return {
                "locked": False
            }

        locked = (
            security_lockout_manager
            .record_failure(
                principal_id
            )
        )

        security_event_log.add(
            SecurityEvent(
                event_type=(
                    "login_failure"
                ),
                source=principal_id,
                severity=(
                    "warning"
                    if not locked
                    else "critical"
                ),
                details={
                    "locked": locked,
                },
            )
        )

        return {
            "locked": locked
        }


security_access_protection_service = (
    SecurityAccessProtectionService()
            )
