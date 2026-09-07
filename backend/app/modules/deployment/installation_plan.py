from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentInstallationPlan:
    target: str

    root_path: str

    steps: list[
        dict[str, Any]
    ] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_step(
        self,
        name: str,
        action: str,
        required: bool = True,
    ):
        step = {
            "name": name,
            "action": action,
            "required": required,
        }

        self.steps.append(
            step
        )

        return step

    def to_dict(self):
        return {
            "target": self.target,
            "root_path": (
                self.root_path
            ),
            "steps": [
                dict(step)
                for step
                in self.steps
            ],
            "metadata": dict(
                self.metadata
            ),
        }
