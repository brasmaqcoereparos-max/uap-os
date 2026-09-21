from __future__ import annotations

from typing import Any

from app.modules.education.schemas import (
    AssessmentResult,
    LearningProfile,
)


class LearningProfileService:

    VALID_LEVELS = {
        "beginner",
        "intermediate",
        "professional",
    }

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

        normalized_user_id = str(
            user_id
        ).strip()

        if not normalized_user_id:
            raise ValueError(
                "user_id is required"
            )

        if (
            normalized_user_id
            in self._profiles
        ):
            return self._profiles[
                normalized_user_id
            ]

        if (
            level
            not in self.VALID_LEVELS
        ):
            raise ValueError(
                "Invalid education level"
            )

        profile = LearningProfile(
            user_id=(
                normalized_user_id
            ),
            level=level,
        )

        self._profiles[
            normalized_user_id
        ] = profile

        return profile

    def get(
        self,
        user_id: str,
    ):

        return self._profiles.get(
            user_id
        )

    def set_level(
        self,
        user_id: str,
        level: str,
    ):

        if (
            level
            not in self.VALID_LEVELS
        ):
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

    def reopen_lesson(
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
            in profile
            .completed_lessons
        ):
            profile.completed_lessons.remove(
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

        previous = (
            profile.scores.get(
                result.exercise_id
            )
        )

        if (
            previous is None
            or result.score
            > previous
        ):
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

    def reset_exercise(
        self,
        user_id: str,
        exercise_id: str,
    ):

        profile = (
            self.get_or_create(
                user_id
            )
        )

        if (
            exercise_id
            in profile.completed_exercises
        ):
            profile.completed_exercises.remove(
                exercise_id
            )

        profile.scores.pop(
            exercise_id,
            None,
        )

        return profile

    def export_profile(
        self,
        user_id: str,
    ) -> dict[str, Any]:

        profile = (
            self.get_or_create(
                user_id
            )
        )

        return profile.model_dump()

    def import_profile(
        self,
        data: dict[str, Any],
        *,
        replace: bool = True,
    ):

        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "Profile data must be a dict"
            )

        profile = LearningProfile(
            **data
        )

        if (
            profile.level
            not in self.VALID_LEVELS
        ):
            raise ValueError(
                "Invalid education level"
            )

        existing = self.get(
            profile.user_id
        )

        if (
            existing is not None
            and not replace
        ):
            return existing

        self._profiles[
            profile.user_id
        ] = profile

        return profile

    def export_all(
        self,
    ) -> dict[str, Any]:

        return {
            user_id: (
                profile.model_dump()
            )
            for (
                user_id,
                profile,
            ) in self._profiles.items()
        }

    def import_all(
        self,
        profiles: dict[
            str,
            Any,
        ],
        *,
        replace: bool = True,
    ):

        if not isinstance(
            profiles,
            dict,
        ):
            raise TypeError(
                "Profiles must be a dict"
            )

        imported = []

        for (
            user_id,
            data,
        ) in profiles.items():

            if not isinstance(
                data,
                dict,
            ):
                continue

            normalized = dict(
                data
            )

            normalized.setdefault(
                "user_id",
                user_id,
            )

            profile = (
                self.import_profile(
                    normalized,
                    replace=replace,
                )
            )

            imported.append(
                profile
            )

        return imported

    def snapshot(
        self,
        user_id: str,
    ):

        return self.export_profile(
            user_id
        )

    def list_all(self):

        return list(
            self._profiles.values()
        )

    def clear(self):

        self._profiles.clear()


learning_profile_service = (
    LearningProfileService()
        )
