from __future__ import annotations

from typing import Any

from app.modules.ai.automation_assistant_service import (
    ai_automation_assistant_service,
)
from app.modules.ai.hardware_assistant_service import (
    ai_hardware_assistant_service,
)
from app.modules.ai.project_builder_service import (
    ai_project_builder_service,
)
from app.modules.ai.safety_service import (
    ai_safety_service,
)
from app.modules.ai.ui_assistant_service import (
    ai_ui_assistant_service,
)


class AIProjectGeneratorService:

    def generate(
        self,
        name: str,
        objective: str,
        *,
        project_requirements: (
            list[dict[str, Any]] | None
        ) = None,
        ui_request: str | None = None,
        ui_preferences: (
            dict[str, Any] | None
        ) = None,
        automation_request: (
            str | None
        ) = None,
        automation_entities: (
            dict[str, Any] | None
        ) = None,
        hardware_requirements: (
            dict[str, Any] | None
        ) = None,
        boards: (
            list[dict[str, Any]] | None
        ) = None,
    ) -> dict[str, Any]:
        project = (
            ai_project_builder_service
            .create(
                name=name,
                objective=objective,
                requirements=(
                    project_requirements
                ),
            )
        )

        result: dict[str, Any] = {
            "project": (
                project.to_dict()
            ),
            "ui": None,
            "automation": None,
            "hardware": None,
            "execution": {
                "direct_execution": False,
                "direct_hardware": False,
                "requires_validation": True,
                "requires_review": True,
                "approved": False,
            },
        }

        if ui_request:
            result["ui"] = (
                ai_ui_assistant_service
                .propose(
                    text=ui_request,
                    app_type="uap",
                    preferences=(
                        ui_preferences
                    ),
                )
            )

        if automation_request:
            result["automation"] = (
                ai_automation_assistant_service
                .propose(
                    text=(
                        automation_request
                    ),
                    objective=objective,
                    entities=(
                        automation_entities
                    ),
                )
            )

        if (
            hardware_requirements
            is not None
        ):
            result["hardware"] = (
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

        safety = (
            ai_safety_service.inspect(
                result
            )
        )

        result["safety"] = (
            safety.to_dict()
        )

        result[
            "ready_for_review"
        ] = (
            project.valid
            and (
                safety.status
                != "blocked"
            )
        )

        result[
            "ready_for_execution"
        ] = False

        return result

    def approve(
        self,
        proposal: dict[str, Any],
    ) -> dict[str, Any]:
        if not isinstance(
            proposal,
            dict,
        ):
            raise TypeError(
                "proposal must be a dict"
            )

        safety = (
            ai_safety_service.approve(
                proposal
            )
        )

        approved = bool(
            safety.accepted
        )

        result = dict(
            proposal
        )

        execution = dict(
            result.get(
                "execution",
                {},
            )
        )

        execution[
            "direct_execution"
        ] = False

        execution[
            "direct_hardware"
        ] = False

        execution[
            "requires_validation"
        ] = True

        execution[
            "requires_review"
        ] = not approved

        execution[
            "approved"
        ] = approved

        result[
            "execution"
        ] = execution

        result[
            "safety"
        ] = safety.to_dict()

        result[
            "ready_for_execution"
        ] = approved

        return result


ai_project_generator_service = (
    AIProjectGeneratorService()
    )
