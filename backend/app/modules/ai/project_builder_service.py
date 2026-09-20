from app.modules.ai.project_builder import (
    ai_project_builder,
)
from app.modules.ai.structured_output_guard import (
    ai_structured_output_guard,
)
from app.modules.ai.structured_result import (
    AIStructuredResult,
)


class AIProjectBuilderService:

    REQUIRED_PROJECT_KEYS = [
        "id",
        "name",
        "objective",
        "requirements",
        "hardware",
        "software",
        "ui",
        "automation",
        "risks",
        "tests",
    ]

    def create(
        self,
        name: str,
        objective: str,
        requirements: (
            list[dict] | None
        ) = None,
    ):
        normalized_name = str(
            name
        ).strip()

        normalized_objective = str(
            objective
        ).strip()

        if not normalized_name:
            return AIStructuredResult(
                result_type=(
                    "project_spec"
                ),
                valid=False,
                errors=[
                    "Project name is required"
                ],
            )

        if not normalized_objective:
            return AIStructuredResult(
                result_type=(
                    "project_spec"
                ),
                valid=False,
                errors=[
                    "Project objective "
                    "is required"
                ],
            )

        project = (
            ai_project_builder.build(
                name=normalized_name,
                objective=(
                    normalized_objective
                ),
                requirements=(
                    requirements
                ),
            )
        )

        data = project.to_dict()

        validation = (
            ai_structured_output_guard
            .validate(
                data,
                required_keys=(
                    self.REQUIRED_PROJECT_KEYS
                ),
            )
        )

        warnings = []

        safety = validation[
            "safety"
        ]

        if (
            safety.get(
                "level"
            )
            == "requires_review"
        ):
            warnings.append(
                "Project requires "
                "safety review"
            )

        errors = []

        if not validation[
            "schema"
        ][
            "valid"
        ]:
            errors.append(
                "Project schema is incomplete"
            )

        if (
            safety.get(
                "level"
            )
            == "blocked"
        ):
            errors.append(
                "Project contains blocked "
                "operations"
            )

        data[
            "validation"
        ] = {
            "schema": (
                validation[
                    "schema"
                ]
            ),
            "safety": safety,
        }

        return AIStructuredResult(
            result_type="project_spec",
            data=data,
            valid=not errors,
            warnings=warnings,
            errors=errors,
        )


ai_project_builder_service = (
    AIProjectBuilderService()
)
