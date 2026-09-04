from dataclasses import dataclass
from dataclasses import field

from app.modules.ai.safety_finding import (
    AISafetyFinding,
)
from app.modules.ai.safety_level import (
    AISafetyLevel,
)


@dataclass
class AISafetyResult:
    level: AISafetyLevel

    findings: list[
        AISafetyFinding
    ] = field(
        default_factory=list
    )

    approved: bool = False

    def add_finding(
        self,
        finding: AISafetyFinding,
    ):
        self.findings.append(
            finding
        )

        if (
            finding.level
            == "blocked"
        ):
            self.level = (
                AISafetyLevel.BLOCKED
            )

        elif (
            finding.level
            == "warning"
            and self.level
            == AISafetyLevel.SAFE
        ):
            self.level = (
                AISafetyLevel
                .REQUIRES_REVIEW
            )

        return finding

    def to_dict(self):
        return {
            "level": self.level.value,
            "approved": (
                self.approved
            ),
            "findings": [
                finding.to_dict()
                for finding
                in self.findings
            ],
          }
