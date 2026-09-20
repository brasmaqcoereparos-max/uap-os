from __future__ import annotations

from typing import Any

from app.modules.ai.context_prompt import (
    ai_context_prompt,
)
from app.modules.ai.planner_service import (
    ai_planner_service,
)
from app.modules.ai.project_autocorrect import (
    ai_project_autocorrect,
)
from app.modules.ai.project_diagnostics import (
    ai_project_diagnostics,
)
from app.modules.ai.project_explainer import (
    ai_project_explainer,
)
from app.modules.ai.project_generator_service import (
    ai_project_generator_service,
)
from app.modules.ai.schemas import (
    AIMessage,
    AIRequest,
    MessageRole,
)
from app.modules.ai.service import (
    ai_service,
)
from app.modules.ai.session_service import (
    ai_session_service,
)


class AIAssistantService:

    def ask(
        self,
        session_id: str,
        text: str,
        provider_name: (
            str | None
        ) = None,
        model: (
            str | None
        ) = None,
    ):
        context = (
            ai_session_service
            .get_context(
                session_id
            )
        )

        conversation = (
            ai_session_service
            .get_conversation(
                session_id
            )
        )

        if not conversation:
            raise ValueError(
                "AI conversation not found"
            )

        normalized_text = str(
            text
        ).strip()

        if not normalized_text:
            raise ValueError(
                "Assistant text "
                "cannot be empty"
            )

        ai_session_service.add_user_message(
            session_id,
            normalized_text,
        )

        request = AIRequest(
            model=model
        )

        context_text = (
            ai_context_prompt.build(
                context
            )
        )

        if context_text:
            request.messages.append(
                AIMessage(
                    role=(
                        MessageRole.SYSTEM
                    ),
                    content=context_text,
                )
            )

        for message in (
            conversation.messages
        ):
            request.messages.append(
                message
            )

        response = (
            ai_service.generate(
                request=request,
                provider_name=(
                    provider_name
                ),
            )
        )

        if response.success:
            ai_session_service.add_assistant_message(
                session_id,
                response.text,
            )

        return response

    def plan_project(
        self,
        title: str,
        description: str = "",
        task_type: str = "project",
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        return (
            ai_planner_service.plan(
                title=title,
                description=description,
                task_type=task_type,
                parameters=parameters,
            )
        )

    def generate_project(
        self,
        name: str,
        objective: str,
        *,
        project_requirements: (
            list[dict[str, Any]] | None
        ) = None,
        ui_request: (
            str | None
        ) = None,
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
    ):
        return (
            ai_project_generator_service
            .generate(
                name=name,
                objective=objective,
                project_requirements=(
                    project_requirements
                ),
                ui_request=(
                    ui_request
                ),
                ui_preferences=(
                    ui_preferences
                ),
                automation_request=(
                    automation_request
                ),
                automation_entities=(
                    automation_entities
                ),
                hardware_requirements=(
                    hardware_requirements
                ),
                boards=boards,
            )
        )

    def diagnose_project(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_project_diagnostics
            .inspect(
                project
            )
        )

    def explain_project(
        self,
        project: dict[str, Any],
        *,
        level: str = "beginner",
        language: str = "pt-BR",
    ):
        return (
            ai_project_explainer
            .explain(
                project=project,
                level=level,
                language=language,
            )
        )

    def propose_corrections(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_project_autocorrect
            .propose(
                project
            )
        )

    def apply_safe_corrections(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_project_autocorrect
            .apply_safe(
                project
            )
        )

    def approve_project_proposal(
        self,
        proposal: dict[str, Any],
    ):
        return (
            ai_project_generator_service
            .approve(
                proposal
            )
        )

    def project_assistance(
        self,
        project: dict[str, Any],
        *,
        level: str = "beginner",
        language: str = "pt-BR",
    ):
        diagnostics = (
            self.diagnose_project(
                project
            )
        )

        explanation = (
            self.explain_project(
                project,
                level=level,
                language=language,
            )
        )

        corrections = (
            self.propose_corrections(
                project
            )
        )

        return {
            "diagnostics": diagnostics,
            "explanation": explanation,
            "corrections": corrections,
            "automatic_execution": False,
            "direct_hardware": False,
            "requires_review": True,
        }


ai_assistant_service = (
    AIAssistantService()
        )
