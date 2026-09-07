from dataclasses import dataclass
from dataclasses import field

from app.modules.deployment.requirement_check import (
    DeploymentRequirementCheck,
)


@dataclass
class DeploymentReadinessResult:
    ready: bool

    checks: list[
        DeploymentRequirementCheck
    ] = field(
        default_factory=list
    )

    def failed(self):
        return [
            check
            for check in self.checks
            if (
                check.required
                and not check.passed
            )
        ]

    def warnings(self):
        return [
            check
            for check in self.checks
            if (
                not check.required
                and not check.passed
            )
        ]

    def to_dict(self):
        return {
            "ready": self.ready,
            "checks": [
                check.to_dict()
                for check
                in self.checks
            ],
            "failed": [
                check.to_dict()
                for check
                in self.failed()
            ],
            "warnings": [
                check.to_dict()
                for check
                in self.warnings()
            ],
              }
