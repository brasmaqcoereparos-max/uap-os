import time

from app.modules.communication.retry_policy import (
    CommunicationRetryPolicy,
)


class CommunicationRetryExecutor:

    def execute(
        self,
        operation,
        policy: (
            CommunicationRetryPolicy
            | None
        ) = None,
    ):
        policy = (
            policy
            or CommunicationRetryPolicy()
        )

        last_error = None

        for attempt in range(
            1,
            policy.max_attempts + 1,
        ):
            try:
                return {
                    "success": True,
                    "attempts": attempt,
                    "result": operation(),
                    "error": None,
                }

            except Exception as exc:
                last_error = exc

                if (
                    attempt
                    >= policy.max_attempts
                ):
                    break

                time.sleep(
                    policy.delay_for(
                        attempt
                    )
                )

        return {
            "success": False,
            "attempts": (
                policy.max_attempts
            ),
            "result": None,
            "error": (
                str(last_error)
                if last_error
                else "Unknown error"
            ),
        }


communication_retry_executor = (
    CommunicationRetryExecutor()
)
