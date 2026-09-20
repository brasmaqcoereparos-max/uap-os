from app.modules.ai.hardware_assistant_service import (
    ai_hardware_assistant_service,
)
from app.modules.ai.project_builder_service import (
    ai_project_builder_service,
)
from app.modules.ai.safety_service import (
    ai_safety_service,
)


class AIProjectArchitect:

    def design(
        self,
        name: str,
        objective: str,
        project_requirements: (
            list[dict] | None
        ) = None,
        hardware_requirements: (
            dict | None
        ) = None,
        boards: (
            list[dict] | None
        ) = None,
    ):
        project_result = (
            ai_project_builder_service
            .create(
                name=name,
                objective=objective,
                requirements=(
                    project_requirements
                ),
            )
        )

        hardware = None

        if (
            hardware_requirements
            is not None
        ):
            hardware = (
                ai_hardware_assistant_service
                .recommend(
                    requirements=(
                        hardware_requirements
                    ),
                    boards=(
                        boards or []
                    ),
                )
            )

        project_data = (
            project_result.to_dict()
        )

        architecture = {
            "project": (
                project_data
            ),
            "hardware": hardware,
            "execution": {
                "direct_hardware": False,
                "requires_validation": True,
                "requires_approval": True,
            },
        }

        safety = (
            ai_safety_service.inspect(
                architecture
            )
        )

        architecture[
            "safety"
        ] = safety.to_dict()

        architecture[
            "ready_for_execution"
        ] = (
            project_result.valid
            and safety.accepted
            and not architecture[
                "execution"
            ][
                "requires_approval"
            ]
        )

        return architecture


ai_project_architect = (
    AIProjectArchitect()
)
