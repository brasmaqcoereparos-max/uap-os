from __future__ import annotations

from typing import Any

from app.modules.education.ai_teacher_bridge import (
    education_ai_teacher_bridge,
)
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
from app.modules.education.progression_service import (
    progression_service,
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

        level = "beginner"

        progression = None

        if user_id:

            profile = (
                learning_profile_service
                .get_or_create(
                    user_id
                )
            )

            level = profile.level

            progression = (
                progression_service
                .lesson_status(
                    user_id,
                    lesson_id,
                )
            )

            if not progression[
                "unlocked"
            ]:
                return {
                    "lesson": (
                        lesson.model_dump()
                    ),
                    "user_level": (
                        level
                    ),
                    "locked": True,
                    "progression": (
                        progression
                    ),
                    "ai_teacher": None,
                    "exercises": [],
                }

        explanation = (
            education_ai_teacher_bridge
            .explain(
                topic=lesson.title,
                level=level,
                context={
                    "lesson_id": (
                        lesson.id
                    ),
                    "description": (
                        lesson.description
                    ),
                    "objectives": list(
                        lesson.objectives
                    ),
                },
            )
        )

        return {
            "lesson": (
                lesson.model_dump()
            ),
            "user_level": level,
            "locked": False,
            "progression": (
                progression
            ),
            "explanation_mode": (
                self._explanation_mode(
                    level
                )
            ),
            "ai_teacher": (
                explanation
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

    def ask(
        self,
        *,
        topic: str,
        question: str,
        user_id: str | None = None,
        level: str | None = None,
        context: dict | None = None,
    ):

        resolved_level = (
            level
            or "beginner"
        )

        if user_id:

            profile = (
                learning_profile_service
                .get_or_create(
                    user_id
                )
            )

            resolved_level = (
                profile.level
            )

        return (
            education_ai_teacher_bridge
            .explain(
                topic=topic,
                question=question,
                level=resolved_level,
                context=context,
            )
        )

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

            exercise = (
                exercise_service.complete(
                    exercise_id
                )
            )

            if (
                progression_service
                .can_complete_lesson(
                    user_id,
                    exercise.lesson_id,
                )
            ):
                progression_service.complete_lesson(
                    user_id,
                    exercise.lesson_id,
                )

        return {
            "assessment": (
                result.model_dump()
            ),
            "progress": (
                progression_service
                .progress(
                    user_id
                )
            ),
        }

    def recommendations(
        self,
        user_id: str,
    ):

        progress = (
            progression_service.progress(
                user_id
            )
        )

        return {
            "user_id": user_id,
            "level": (
                progress[
                    "level"
                ]
            ),
            "progress_percent": (
                progress[
                    "progress_percent"
                ]
            ),
            "mastery": (
                progress[
                    "mastery"
                ]
            ),
            "next_lessons": (
                progress[
                    "next_lessons"
                ]
            ),
        }

    def start_lab(
        self,
        scenario_id: str,
    ):

        return lab_service.start(
            scenario_id
        )

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


ai_teacher_service = (
    AITeacherService()
            )
