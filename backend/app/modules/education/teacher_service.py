from __future__ import annotations

from typing import Any

from app.modules.education.assessment_service import (
    assessment_service,
)
from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.lab_service import (
    lab_service,
)
from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.lesson_service import (
    lesson_service,
)


class AITeacherService:

    def lesson(
        self,
        lesson_id: str,
        user_id: str | None = None,
    ):
        lesson = (
            lesson_service.require(
                lesson_id
            )
        )

        level = (
            "beginner"
        )

        if user_id:
            profile = (
                learning_profile_service
                .get_or_create(
                    user_id
                )
            )

            level = profile.level

        return {
            "lesson": (
                lesson.model_dump()
            ),
            "user_level": level,
            "explanation_mode": (
                self._explanation_mode(
                    level
                )
            ),
            "exercises": [
                exercise.model_dump()
                for exercise
                in exercise_service
                .for_lesson(
                    lesson_id
                )
            ],
        }

    def _explanation_mode(
        self,
        level: str,
    ):
        if level == "beginner":
            return {
                "language": "simple",
                "code_required": False,
                "show_visual_steps": True,
                "show_advanced_details": False,
            }

        if level == "intermediate":
            return {
                "language": "guided",
                "code_required": False,
                "show_visual_steps": True,
                "show_advanced_details": True,
            }

        return {
            "language": "technical",
            "code_required": False,
            "show_visual_steps": True,
            "show_advanced_details": True,
        }

    def assess(
        self,
        user_id: str,
        exercise_id: str,
        answer: dict[str, Any],
    ):
        result = (
            assessment_service.assess(
                exercise_id,
                answer,
            )
        )

        learning_profile_service.record_assessment(
            user_id,
            result,
        )

        if result.passed:
            exercise_service.complete(
                exercise_id
            )

        return result

    def start_lab(
        self,
        scenario_id: str,
    ):
        return lab_service.start(
            scenario_id
        )


ai_teacher_service = (
    AITeacherService()
)
