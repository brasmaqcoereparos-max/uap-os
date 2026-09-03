import uuid

from app.modules.ai.project_requirement import (
    AIProjectRequirement,
)
from app.modules.ai.project_spec import (
    AIProjectSpec,
)


class AIProjectBuilder:

    def build(
        self,
        name: str,
        objective: str,
        requirements: (
            list[dict] | None
        ) = None,
    ):
        project = AIProjectSpec(
            id=str(uuid.uuid4()),
            name=name,
            objective=objective,
        )

        for index, item in enumerate(
            requirements or [],
            start=1,
        ):
            requirement = (
                AIProjectRequirement(
                    id=str(
                        item.get(
                            "id",
                            f"req-{index}",
                        )
                    ),
                    name=str(
                        item.get(
                            "name",
                            f"Requirement {index}",
                        )
                    ),
                    requirement_type=str(
                        item.get(
                            "requirement_type",
                            "general",
                        )
                    ),
                    description=str(
                        item.get(
                            "description",
                            "",
                        )
                    ),
                    required=bool(
                        item.get(
                            "required",
                            True,
                        )
                    ),
                    value=item.get(
                        "value"
                    ),
                    metadata=dict(
                        item.get(
                            "metadata",
                            {},
                        )
                    ),
                )
            )

            project.add_requirement(
                requirement
            )

        return project


ai_project_builder = (
    AIProjectBuilder()
                        )
