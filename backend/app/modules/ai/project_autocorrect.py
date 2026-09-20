from __future__ import annotations

from copy import deepcopy
from typing import Any

from app.modules.ai.project_diagnostics import (
    ai_project_diagnostics,
)


class AIProjectAutocorrect:

    SAFE_CORRECTIONS = {
        "missing_requirements",
        "missing_tests",
        "hardware_not_defined",
    }

    def analyze(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_project_diagnostics
            .inspect(
                project
            )
        )

    def propose(
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

        diagnostics = (
            self.analyze(
                project
            )
        )

        corrections = []

        for finding in (
            diagnostics[
                "findings"
            ]
        ):
            code = finding[
                "code"
            ]

            if (
                code
                not in self.SAFE_CORRECTIONS
            ):
                continue

            correction = (
                self._correction_for(
                    code
                )
            )

            if correction:
                corrections.append(
                    correction
                )

        return {
            "project": deepcopy(
                project
            ),
            "diagnostics": (
                diagnostics
            ),
            "corrections": (
                corrections
            ),
            "requires_review": (
                bool(
                    corrections
                )
            ),
            "applied": False,
        }

    def apply_safe(
        self,
        project: dict[str, Any],
    ) -> dict[str, Any]:
        proposal = self.propose(
            project
        )

        corrected = deepcopy(
            project
        )

        applied = []

        for correction in (
            proposal[
                "corrections"
            ]
        ):
            action = correction[
                "action"
            ]

            if action == (
                "add_empty_requirements"
            ):
                corrected.setdefault(
                    "requirements",
                    [],
                )

            elif action == (
                "add_validation_tests"
            ):
                corrected.setdefault(
                    "tests",
                    [
                        {
                            "name": (
                                "simulation"
                            ),
                            "required": True,
                        },
                        {
                            "name": (
                                "safety_boundary"
                            ),
                            "required": True,
                        },
                    ],
                )

            elif action == (
                "mark_hardware_pending"
            ):
                corrected.setdefault(
                    "hardware",
                    {
                        "status": (
                            "pending_selection"
                        ),
                    },
                )

            else:
                continue

            applied.append(
                correction
            )

        return {
            "project": corrected,
            "before": (
                proposal[
                    "diagnostics"
                ]
            ),
            "after": (
                self.analyze(
                    corrected
                )
            ),
            "applied": applied,
            "requires_review": True,
            "automatic_execution": False,
            "direct_hardware": False,
        }

    def _correction_for(
        self,
        code: str,
    ):
        mapping = {
            "missing_requirements": {
                "code": (
                    "missing_requirements"
                ),
                "action": (
                    "add_empty_requirements"
                ),
                "description": (
                    "Create requirements "
                    "container"
                ),
            },
            "missing_tests": {
                "code": "missing_tests",
                "action": (
                    "add_validation_tests"
                ),
                "description": (
                    "Add minimum simulation "
                    "and safety tests"
                ),
            },
            "hardware_not_defined": {
                "code": (
                    "hardware_not_defined"
                ),
                "action": (
                    "mark_hardware_pending"
                ),
                "description": (
                    "Mark hardware selection "
                    "as pending"
                ),
            },
        }

        return mapping.get(
            code
        )


ai_project_autocorrect = (
    AIProjectAutocorrect()
                )
