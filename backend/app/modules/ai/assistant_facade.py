from __future__ import annotations

from typing import Any

from app.modules.ai.assistant_capabilities import (
    ai_assistant_capabilities,
)
from app.modules.ai.assistant_service import (
    ai_assistant_service,
)
from app.modules.ai.session_service import (
    ai_session_service,
)


class AIAssistantFacade:

    def create_session(
        self,
        user_id: (
            str | None
        ) = None,
        project_id: (
            str | None
        ) = None,
        user_level: (
            str | None
        ) = None,
    ):
        return (
            ai_session_service
            .create_session(
                user_id=user_id,
                project_id=project_id,
                user_level=user_level,
            )
        )

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
        return (
            ai_assistant_service
            .ask(
                session_id=session_id,
                text=text,
                provider_name=(
                    provider_name
                ),
                model=model,
            )
        )

    def capabilities(self):
        return (
            ai_assistant_capabilities
            .list_all()
        )

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
            ai_assistant_service
            .plan_project(
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
        **kwargs,
    ):
        return (
            ai_assistant_service
            .generate_project(
                name=name,
                objective=objective,
                **kwargs,
            )
        )

    def diagnose_project(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_assistant_service
            .diagnose_project(
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
            ai_assistant_service
            .explain_project(
                project,
                level=level,
                language=language,
            )
        )

    def propose_corrections(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_assistant_service
            .propose_corrections(
                project
            )
        )

    def apply_safe_corrections(
        self,
        project: dict[str, Any],
    ):
        return (
            ai_assistant_service
            .apply_safe_corrections(
                project
            )
        )

    def approve_project_proposal(
        self,
        proposal: dict[str, Any],
    ):
        return (
            ai_assistant_service
            .approve_project_proposal(
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
        return (
            ai_assistant_service
            .project_assistance(
                project,
                level=level,
                language=language,
            )
        )


ai_assistant_facade = (
    AIAssistantFacade()
            )
