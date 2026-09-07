from datetime import datetime
from datetime import timedelta
from datetime import timezone

from app.modules.security.lockout_policy import (
    security_lockout_policy,
)


class SecurityLockoutManager:

    def __init__(self):
        self._failures: dict[
            str,
            list[datetime],
        ] = {}

        self._locked_until: dict[
            str,
            datetime,
        ] = {}

    def record_failure(
        self,
        principal_id: str,
    ):
        now = datetime.now(
            timezone.utc
        )

        failures = (
            self._failures
            .setdefault(
                principal_id,
                [],
            )
        )

        failures.append(
            now
        )

        failures[:] = [
            item
            for item in failures
            if (
                now - item
            ).total_seconds()
            <= (
                security_lockout_policy
                .lockout_seconds
            )
        ]

        if len(failures) >= (
            security_lockout_policy
            .max_failures
        ):
            self._locked_until[
                principal_id
            ] = (
                now
                + timedelta(
                    seconds=(
                        security_lockout_policy
                        .lockout_seconds
                    )
                )
            )

        return self.is_locked(
            principal_id
        )

    def clear(
        self,
        principal_id: str,
    ):
        self._failures.pop(
            principal_id,
            None,
        )

        self._locked_until.pop(
            principal_id,
            None,
        )

    def is_locked(
        self,
        principal_id: str,
    ):
        locked_until = (
            self._locked_until.get(
                principal_id
            )
        )

        if not locked_until:
            return False

        now = datetime.now(
            timezone.utc
        )

        if now >= locked_until:
            self.clear(
                principal_id
            )

            return False

        return True


security_lockout_manager = (
    SecurityLockoutManager()
      )
