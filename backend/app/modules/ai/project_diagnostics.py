from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class AIDiagnosticFinding:
    code: str
    message: str

    level: str = "warning"

    path: str | None = None

    suggestion: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "level": self.level,
            "path": self.path,
            "suggestion": self.suggestion,
            "metadata": dict(
                self.metadata
            ),
        }


class AIProjectDiagnostics:

    VALID_LEVELS = {
        "info",
        "warning",
        "error",
        "blocked",
    }

    def inspect(
        self,
        project: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(
            project,
            dict,
        ):
            raise TypeError(
                "project must be a dict"
            )

        findings: list[
            AIDiagnosticFinding
        ] = []

        self._check_identity(
            project,
            findings,
        )

        self._check_objective(
            project,
            findings,
        )

        self._check_requirements(
            project,
            findings,
        )

        self._check_hardware(
            project,
            findings,
        )

        self._check_automation(
            project,
            findings,
        )

        self._check_ui(
            project,
            findings,
        )

        self._check_safety(
            project,
            findings,
        )

        self._check_tests(
            project,
            findings,
        )

        errors = [
            finding
            for finding in findings
            if finding.level
            in {
                "error",
                "blocked",
            }
        ]

        warnings = [
            finding
            for finding in findings
            if finding.level
            == "warning"
        ]

        return {
            "valid": not errors,
            "requires_review": bool(
                errors
                or warnings
            ),
            "finding_count": len(
                findings
            ),
            "error_count": len(
                errors
            ),
            "warning_count": len(
                warnings
            ),
            "findings": [
                finding.to_dict()
                for finding
                in findings
            ],
        }

    def _add(
        self,
        findings: list[
            AIDiagnosticFinding
        ],
        *,
        code: str,
        message: str,
        level: str = "warning",
        path: str | None = None,
        suggestion: str | None = None,
    ) -> None:
        if (
            level
            not in self.VALID_LEVELS
        ):
            level = "warning"

        findings.append(
            AIDiagnosticFinding(
                code=code,
                message=message,
                level=level,
                path=path,
                suggestion=suggestion,
            )
        )

    def _check_identity(
        self,
        project,
        findings,
    ):
        if not project.get(
            "name"
        ):
            self._add(
                findings,
                code="missing_name",
                message=(
                    "Project name is missing"
                ),
                level="error",
                path="name",
                suggestion=(
                    "Define a project name"
                ),
            )

    def _check_objective(
        self,
        project,
        findings,
    ):
        if not project.get(
            "objective"
        ):
            self._add(
                findings,
                code=(
                    "missing_objective"
                ),
                message=(
                    "Project objective "
                    "is missing"
                ),
                level="error",
                path="objective",
                suggestion=(
                    "Define the expected "
                    "project result"
                ),
            )

    def _check_requirements(
        self,
        project,
        findings,
    ):
        requirements = (
            project.get(
                "requirements"
            )
        )

        if not requirements:
            self._add(
                findings,
                code=(
                    "missing_requirements"
                ),
                message=(
                    "Project has no "
                    "requirements"
                ),
                level="warning",
                path="requirements",
                suggestion=(
                    "Add functional and "
                    "safety requirements"
                ),
            )

    def _check_hardware(
        self,
        project,
        findings,
    ):
        hardware = project.get(
            "hardware"
        )

        if hardware is None:
            self._add(
                findings,
                code=(
                    "hardware_not_defined"
                ),
                message=(
                    "Hardware definition "
                    "is missing"
                ),
                level="info",
                path="hardware",
                suggestion=(
                    "Select hardware before "
                    "physical deployment"
                ),
            )

    def _check_automation(
        self,
        project,
        findings,
    ):
        automation = (
            project.get(
                "automation"
            )
        )

        if automation is None:
            return

        if not isinstance(
            automation,
            (
                dict,
                list,
            ),
        ):
            self._add(
                findings,
                code=(
                    "invalid_automation"
                ),
                message=(
                    "Automation definition "
                    "has an invalid format"
                ),
                level="error",
                path="automation",
            )

    def _check_ui(
        self,
        project,
        findings,
    ):
        ui = project.get(
            "ui"
        )

        if ui is None:
            return

        if not isinstance(
            ui,
            (
                dict,
                list,
            ),
        ):
            self._add(
                findings,
                code="invalid_ui",
                message=(
                    "UI definition has "
                    "an invalid format"
                ),
                level="error",
                path="ui",
            )

    def _check_safety(
        self,
        project,
        findings,
    ):
        serialized = str(
            project
        ).lower()

        forbidden = (
            "direct_gpio",
            "direct_hardware",
            "hardware.direct_write",
        )

        for token in forbidden:
            if token in serialized:
                self._add(
                    findings,
                    code=(
                        "direct_hardware_access"
                    ),
                    message=(
                        "Project contains "
                        "direct hardware access"
                    ),
                    level="blocked",
                    path="execution",
                    suggestion=(
                        "Route hardware actions "
                        "through Runtime/Safety"
                    ),
                )

                break

    def _check_tests(
        self,
        project,
        findings,
    ):
        if not project.get(
            "tests"
        ):
            self._add(
                findings,
                code="missing_tests",
                message=(
                    "Project has no "
                    "validation tests"
                ),
                level="warning",
                path="tests",
                suggestion=(
                    "Create simulation and "
                    "boundary tests"
                ),
            )


ai_project_diagnostics = (
    AIProjectDiagnostics()
            )
