from __future__ import annotations

from typing import Any

from app.modules.ai.education_assistant import (
    ai_education_assistant,
)
from app.modules.ai.education_profile import (
    AIEducationProfile,
)
from app.modules.ai.education_request import (
    AIEducationRequest,
)


class AIEducationAssistantService:

    VALID_LEVELS = {
        "beginner",
        "intermediate",
        "professional",
    }

    def explain(
        self,
        topic: str,
        question: str = "",
        level: str = "beginner",
        language: str = "pt-BR",
        include_examples: bool = True,
        include_exercises: bool = False,
        context: dict | None = None,
    ):
        normalized_level = str(
            level
        ).strip().lower()

        if (
            normalized_level
            not in self.VALID_LEVELS
        ):
            raise ValueError(
                "Unsupported education level: "
                f"{level}"
            )

        profile = AIEducationProfile(
            level=normalized_level,
            language=language,
            step_by_step=True,
            include_examples=(
                include_examples
            ),
            include_exercises=(
                include_exercises
            ),
        )

        request = AIEducationRequest(
            topic=topic,
            question=question,
            profile=profile,
            context=dict(
                context or {}
            ),
        )

        response = (
            ai_education_assistant
            .explain(
                request
            )
        )

        return {
            "request": (
                request.to_dict()
            ),
            "response": (
                response.to_dict()
            ),
            "target": "education",
            "direct_hardware": False,
            "simulation_first": True,
        }

    def propose_exercise(
        self,
        *,
        topic: str,
        lesson_id: str,
        level: str = "beginner",
    ) -> dict[str, Any]:

        explanation = self.explain(
            topic=topic,
            level=level,
            include_examples=True,
            include_exercises=True,
        )

        suggested = (
            explanation[
                "response"
            ][
                "exercises"
            ]
        )

        return {
            "type": (
                "exercise_proposal"
            ),
            "lesson_id": (
                lesson_id
            ),
            "topic": topic,
            "difficulty": level,
            "title": (
                f"Exercício: {topic}"
            ),
            "description": (
                suggested[0]
                if suggested
                else (
                    "Exercício educacional "
                    f"sobre {topic}."
                )
            ),
            "exercise_type": (
                "simulation"
            ),
            "expected_result": {},
            "requires_review": True,
            "registered": False,
            "direct_hardware": False,
        }

    def propose_lab(
        self,
        *,
        topic: str,
        level: str = "beginner",
    ) -> dict[str, Any]:

        return {
            "type": "lab_proposal",
            "topic": topic,
            "name": (
                f"Laboratório: {topic}"
            ),
            "description": (
                "Laboratório didático "
                f"simulado sobre {topic}."
            ),
            "difficulty": level,
            "simulation_only": True,
            "project_template": {
                "nodes": [],
                "connections": [],
            },
            "expected_state": {},
            "requires_review": True,
            "registered": False,
            "direct_hardware": False,
        }


ai_education_assistant_service = (
    AIEducationAssistantService()
)
