from dataclasses import dataclass
from dataclasses import field


@dataclass
class DeploymentSystemdDefinition:
    service_name: str = "uap-os"

    description: str = "UAP OS Service"

    working_directory: str = ""

    user: str = ""

    command: list[str] = field(
        default_factory=lambda: [
            "python",
            "-m",
            "app.main",
        ]
    )

    environment_file: str | None = None

    wanted_by: str = "multi-user.target"

    def to_dict(self):
        return {
            "service_name": self.service_name,
            "description": self.description,
            "working_directory": (
                self.working_directory
            ),
            "user": self.user,
            "command": list(
                self.command
            ),
            "environment_file": (
                self.environment_file
            ),
            "wanted_by": self.wanted_by,
        }
