from __future__ import annotations

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
from app.modules.education.teacher_service import (
    ai_teacher_service,
)


class EducationService:

    def __init__(self):
        self.education_mode = False

    def enable(self):
        self.education_mode = True

        return self.education_mode

    def disable(self):
        self.education_mode = False

        return self.education_mode

    def status(self):
        return {
            "education_mode": (
                self.education_mode
            ),
            "lessons": len(
                lesson_service.list_all()
            ),
            "exercises": len(
                exercise_service.list_all()
            ),
            "labs": len(
                lab_service.list_all()
            ),
        }

    def lessons(
        self,
        difficulty: str | None = None,
    ):
        return [
            lesson.model_dump()
            for lesson
            in lesson_service.list_all(
                difficulty
            )
        ]

    def lesson(
        self,
        lesson_id: str,
        user_id: str | None = None,
    ):
        return (
            ai_teacher_service.lesson(
                lesson_id,
                user_id,
            )
        )

    def profile(
        self,
        user_id: str,
    ):
        return (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

    def assess(
        self,
        user_id: str,
        exercise_id: str,
        answer: dict,
    ):
        return (
            ai_teacher_service.assess(
                user_id=user_id,
                exercise_id=exercise_id,
                answer=answer,
            )
        )

    def start_lab(
        self,
        scenario_id: str,
    ):
        if not self.education_mode:
            raise RuntimeError(
                "Education mode is disabled"
            )

        return (
            ai_teacher_service
            .start_lab(
                scenario_id
            )
        )


education_service = (
    EducationService()
        )
