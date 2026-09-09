from dataclasses import dataclass
from dataclasses import field


@dataclass
class DeploymentServiceCommand:
    action: str

    command: list[str] = field(
        default_factory=list
    )

    requires_privilege: bool = False

    def to_dict(self):
        return {
            "action": self.action,
            "command": list(
                self.command
            ),
            "requires_privilege": (
                self.requires_privilege
            ),
        }
