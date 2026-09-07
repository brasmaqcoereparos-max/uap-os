from dataclasses import dataclass


@dataclass
class DeploymentRollbackPlan:
    backup_path: str

    target_path: str

    version: str = ""

    requires_stop: bool = True

    requires_restart: bool = True

    def to_dict(self):
        return {
            "backup_path": (
                self.backup_path
            ),
            "target_path": (
                self.target_path
            ),
            "version": self.version,
            "requires_stop": (
                self.requires_stop
            ),
            "requires_restart": (
                self.requires_restart
            ),
        }
