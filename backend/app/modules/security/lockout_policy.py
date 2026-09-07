from dataclasses import dataclass


@dataclass
class SecurityLockoutPolicy:
    max_failures: int = 5

    lockout_seconds: int = 300

    def to_dict(self):
        return {
            "max_failures": (
                self.max_failures
            ),
            "lockout_seconds": (
                self.lockout_seconds
            ),
        }


security_lockout_policy = (
    SecurityLockoutPolicy()
)
