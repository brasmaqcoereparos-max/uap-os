from dataclasses import dataclass


@dataclass
class DeploymentRestartPolicy:
    restart: str = "on-failure"

    restart_seconds: int = 5

    start_limit_interval_seconds: int = 60

    start_limit_burst: int = 5

    def to_dict(self):
        return {
            "restart": self.restart,
            "restart_seconds": (
                self.restart_seconds
            ),
            "start_limit_interval_seconds": (
                self.start_limit_interval_seconds
            ),
            "start_limit_burst": (
                self.start_limit_burst
            ),
        }


deployment_restart_policy = (
    DeploymentRestartPolicy()
)
