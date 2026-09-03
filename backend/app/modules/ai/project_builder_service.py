from app.modules.ai.project_builder import (
    ai_project_builder,
)
from app.modules.ai.structured_result import (
    AIStructuredResult,
)


class AIProjectBuilderService:

    def create(
        self,
        name: str,
        objective: str,
        requirements: (
            list[dict] | None
        ) = None,
    ):
        project = (
            ai_project_builder.build(
                name=name,
                objective=objective,
                requirements=(
                    requirements
                ),
            )
        )

        return AIStructuredResult(
            result_type="project_spec",
            data=project.to_dict(),
            valid=True,
        )


ai_project_builder_service = (
    AIProjectBuilderService()
)
