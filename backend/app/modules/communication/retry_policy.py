from dataclasses import dataclass


@dataclass
class CommunicationRetryPolicy:
    max_attempts: int = 3

    delay_seconds: float = 0.5

    backoff_multiplier: float = 2.0

    max_delay_seconds: float = 10.0

    def delay_for(
        self,
        attempt: int,
    ):
        attempt = max(
            1,
            attempt,
        )

        delay = (
            self.delay_seconds
            * (
                self.backoff_multiplier
                ** (
                    attempt - 1
                )
            )
        )

        return min(
            delay,
            self.max_delay_seconds,
        )

    def to_dict(self):
        return {
            "max_attempts": (
                self.max_attempts
            ),
            "delay_seconds": (
                self.delay_seconds
            ),
            "backoff_multiplier": (
                self.backoff_multiplier
            ),
            "max_delay_seconds": (
                self.max_delay_seconds
            ),
        }
