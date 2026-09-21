from __future__ import annotations

from app.modules.education.schemas import (
    AssessmentResult,
    LearningProfile,
)


class LearningProfileService:

    def __init__(self):
        self._profiles: dict[
            str,
            LearningProfile,
        ] = {}

    def get_or_create(
        self,
        user_id: str,
        level: str = "beginner",
    ):
        if user_id in self._profiles:
            return self._profiles[
                user_id
            ]

        profile = LearningProfile(
            user_id=user_id,
            level=level,
        )

        self._profiles[
            user_id
        ] = profile

        return profile

    def set_level(
        self,
        user_id: str,
        level: str,
    ):
        if level not in {
            "beginner",
            "intermediate",
            "professional",
        }:
            raise ValueError(
                "Invalid education level"
            )

        profile = (
            self.get_or_create(
                user_id
            )
        )

        profile.level = level

        return profile

    def complete_lesson(
        self,
        user_id: str,
        lesson_id: str,
    ):
        profile = (
            self.get_or_create(
                user_id
            )
        )

        if (
            lesson_id
            not in profile
            .completed_lessons
        ):
            profile.completed_lessons.append(
                lesson_id
            )

        return profile

    def record_assessment(
        self,
        user_id: str,
        result: AssessmentResult,
    ):
        profile = (
            self.get_or_create(
                user_id
            )
        )

        profile.scores[
            result.exercise_id
        ] = result.score

        if (
            result.passed
            and result.exercise_id
            not in profile
            .completed_exercises
        ):
            profile.completed_exercises.append(
                result.exercise_id
            )

        return profile

    def get(
        self,
        user_id: str,
    ):
        return self._profiles.get(
            user_id
        )


learning_profile_service = (
    LearningProfileService()
)
