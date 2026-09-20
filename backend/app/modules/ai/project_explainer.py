from __future__ import annotations

from typing import Any

from app.modules.ai.project_diagnostics import (
    ai_project_diagnostics,
)


class AIProjectExplainer:

    LEVELS = {
        "beginner",
        "intermediate",
        "professional",
    }

    def explain(
        self,
        project: dict[str, Any],
        level: str = "beginner",
        language: str = "pt-BR",
    ) -> dict[str, Any]:
        if not isinstance(
            project,
            dict,
        ):
            raise TypeError(
                "project must be a dict"
            )

        normalized_level = str(
            level
        ).strip().lower()

        if (
            normalized_level
            not in self.LEVELS
        ):
            raise ValueError(
                "Unsupported explanation "
                f"level: {level}"
            )

        diagnostics = (
            ai_project_diagnostics
            .inspect(
                project
            )
        )

        sections = (
            self._sections(
                project,
                normalized_level,
            )
        )

        return {
            "project_name": (
                project.get(
                    "name",
                    "Unnamed project",
                )
            ),
            "level": (
                normalized_level
            ),
            "language": language,
            "summary": (
                self._summary(
                    project
                )
            ),
            "sections": sections,
            "diagnostics": (
                diagnostics
            ),
            "requires_review": (
                diagnostics[
                    "requires_review"
                ]
            ),
        }

    def _summary(
        self,
        project,
    ) -> str:
        name = project.get(
            "name",
            "Projeto",
        )

        objective = (
            project.get(
                "objective"
            )
            or "objetivo não definido"
        )

        return (
            f"{name}: {objective}"
        )

    def _sections(
        self,
        project,
        level,
    ):
        sections = [
            {
                "title": "Objetivo",
                "content": (
                    project.get(
                        "objective"
                    )
                    or "Não definido"
                ),
            },
            {
                "title": "Requisitos",
                "content": (
                    project.get(
                        "requirements",
                        [],
                    )
                ),
            },
            {
                "title": "Hardware",
                "content": (
                    project.get(
                        "hardware"
                    )
                    or {
                        "status": (
                            "não definido"
                        )
                    }
                ),
            },
            {
                "title": "Automação",
                "content": (
                    project.get(
                        "automation"
                    )
                    or {
                        "status": (
                            "não definida"
                        )
                    }
                ),
            },
            {
                "title": "Interface",
                "content": (
                    project.get(
                        "ui"
                    )
                    or {
                        "status": (
                            "não definida"
                        )
                    }
                ),
            },
        ]

        if level in {
            "intermediate",
            "professional",
        }:
            sections.append(
                {
                    "title": "Testes",
                    "content": (
                        project.get(
                            "tests",
                            [],
                        )
                    ),
                }
            )

        if (
            level
            == "professional"
        ):
            sections.extend(
                [
                    {
                        "title": (
                            "Metadados"
                        ),
                        "content": (
                            project.get(
                                "metadata",
                                {},
                            )
                        ),
                    },
                    {
                        "title": (
                            "Execução"
                        ),
                        "content": (
                            project.get(
                                "execution",
                                {},
                            )
                        ),
                    },
                ]
            )

        return sections


ai_project_explainer = (
    AIProjectExplainer()
  )
