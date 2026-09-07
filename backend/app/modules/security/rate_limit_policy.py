from dataclasses import dataclass


@dataclass
class SecurityRateLimitPolicy:
    max_requests: int = 60

    window_seconds: int = 60

    def to_dict(self):
        return {
            "max_requests": (
                self.max_requests
            ),
            "window_seconds": (
                self.window_seconds
            ),
        }


security_rate_limit_policy = (
    SecurityRateLimitPolicy()
)
