from datetime import datetime
from datetime import timezone

from app.modules.security.rate_limit_policy import (
    security_rate_limit_policy,
)


class SecurityRateLimiter:

    def __init__(self):
        self._requests: dict[
            str,
            list[datetime],
        ] = {}

    def allow(
        self,
        key: str,
    ):
        now = datetime.now(
            timezone.utc
        )

        requests = (
            self._requests
            .setdefault(
                key,
                [],
            )
        )

        requests[:] = [
            item
            for item in requests
            if (
                now - item
            ).total_seconds()
            <= (
                security_rate_limit_policy
                .window_seconds
            )
        ]

        if len(requests) >= (
            security_rate_limit_policy
            .max_requests
        ):
            return False

        requests.append(
            now
        )

        return True

    def reset(
        self,
        key: str,
    ):
        self._requests.pop(
            key,
            None,
        )


security_rate_limiter = (
    SecurityRateLimiter()
)
