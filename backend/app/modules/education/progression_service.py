from __future__ import annotations

from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.lesson_service import (
    lesson_service,
)
from app.modules.education.mastery_service import (
    mastery_service,
)


class ProgressionService:

    def prerequisites_met(
        self,
        user_id: str,
        lesson_id: str,
    ) -> bool:

        lesson = (
            lesson_service.require(
                lesson_id
            )
        )

        if not lesson.prerequisites:
            return True

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        completed = set(
            profile.completed_lessons
        )

        return all(
            prerequisite
            in completed
            for prerequisite
            in lesson.prerequisites
        )

    def missing_prerequisites(
        self,
        user_id: str,
        lesson_id: str,
    ) -> list[str]:

        lesson = (
            lesson_service.require(
                lesson_id
            )
        )

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        completed = set(
            profile.completed_lessons
        )

        return [
            prerequisite
            for prerequisite
            in lesson.prerequisites
            if prerequisite
            not in completed
        ]

    def lesson_score(
        self,
        user_id: str,
        lesson_id: str,
    ) -> float | None:

        exercises = (
            exercise_service
            .for_lesson(
                lesson_id
            )
        )

        exercise_ids = [
            exercise.id
            for exercise
            in exercises
        ]

        return (
            mastery_service
            .lesson_score(
                user_id,
                exercise_ids,
            )
        )

    def can_complete_lesson(
        self,
        user_id: str,
        lesson_id: str,
    ) -> bool:

        if not self.prerequisites_met(
            user_id,
            lesson_id,
        ):
            return False

        exercises = (
            exercise_service
            .for_lesson(
                lesson_id
            )
        )

        if not exercises:
            return True

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        completed = set(
            profile.completed_exercises
        )

        return all(
            exercise.id
            in completed
            for exercise
            in exercises
        )

    def complete_lesson(
        self,
        user_id: str,
        lesson_id: str,
    ):

        lesson_service.require(
            lesson_id
        )

        if not self.can_complete_lesson(
            user_id,
            lesson_id,
        ):
            raise RuntimeError(
                "Lesson requirements "
                "are not complete"
            )

        return (
            learning_profile_service
            .complete_lesson(
                user_id,
                lesson_id,
            )
        )

    def lesson_status(
        self,
        user_id: str,
        lesson_id: str,
    ):

        lesson = (
            lesson_service.require(
                lesson_id
            )
        )

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        score = self.lesson_score(
            user_id,
            lesson_id,
        )

        completed = (
            lesson_id
            in profile.completed_lessons
        )

        prerequisites_met = (
            self.prerequisites_met(
                user_id,
                lesson_id,
            )
        )

        return {
            "lesson_id": lesson_id,
            "difficulty": (
                lesson.difficulty
            ),
            "unlocked": (
                prerequisites_met
            ),
            "prerequisites_met": (
                prerequisites_met
            ),
            "missing_prerequisites": (
                self.missing_prerequisites(
                    user_id,
                    lesson_id,
                )
            ),
            "can_complete": (
                self.can_complete_lesson(
                    user_id,
                    lesson_id,
                )
            ),
            "completed": completed,
            "score": score,
            "mastery": (
                mastery_service
                .level_for_score(
                    score
                )
            ),
        }

    def available_lessons(
        self,
        user_id: str,
    ):

        return [
            lesson
            for lesson
            in lesson_service.list_all()
            if self.prerequisites_met(
                user_id,
                lesson.id,
            )
        ]

    def next_lessons(
        self,
        user_id: str,
    ):

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        completed = set(
            profile.completed_lessons
        )

        return [
            lesson
            for lesson
            in self.available_lessons(
                user_id
            )
            if lesson.id
            not in completed
        ]

    def progress(
        self,
        user_id: str,
    ):

        lessons = (
            lesson_service.list_all()
        )

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        total = len(
            lessons
        )

        completed = len(
            [
                lesson_id
                for lesson_id
                in profile.completed_lessons
                if lesson_service.get(
                    lesson_id
                )
                is not None
            ]
        )

        percentage = (
            completed
            / total
            * 100.0
            if total
            else 0.0
        )

        return {
            "user_id": user_id,
            "level": profile.level,
            "total_lessons": total,
            "completed_lessons": (
                completed
            ),
            "progress_percent": (
                round(
                    percentage,
                    2,
                )
            ),
            "mastery": (
                mastery_service
                .summary(
                    user_id
                )
            ),
            "next_lessons": [
                lesson.id
                for lesson
                in self.next_lessons(
                    user_id
                )
            ],
        }


progression_service = (
    ProgressionService()
      )
