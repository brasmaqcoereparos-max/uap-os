from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentRequirementCheck:
    name: str

    passed: bool

    required: bool = True

    message: str = ""

    details: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "name": self.name,
            "passed": self.passed,
            "required": self.required,
            "message": self.message,
            "details": dict(
                self.details
            ),
        }
