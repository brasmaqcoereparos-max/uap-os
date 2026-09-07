from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentStartupDefinition:
    name: str = "uap-os"

    enabled: bool = True

    restart_on_failure: bool = True

    command: list[str] = field(
        default_factory=lambda: [
            "python",
            "-m",
            "app.main",
        ]
    )

    environment: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "enabled": self.enabled,
            "restart_on_failure": (
                self.restart_on_failure
            ),
            "command": list(
                self.command
            ),
            "environment": dict(
                self.environment
            ),
        }
