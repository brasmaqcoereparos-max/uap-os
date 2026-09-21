from __future__ import annotations

from statistics import mean

from app.modules.education.learning_profile_service import (
    learning_profile_service,
)


class MasteryService:

    PASS_SCORE = 70.0

    MASTERY_SCORE = 85.0

    def exercise_score(
        self,
        user_id: str,
        exercise_id: str,
    ) -> float | None:

        profile = (
            learning_profile_service
            .get(
                user_id
            )
        )

        if profile is None:
            return None

        score = profile.scores.get(
            exercise_id
        )

        if score is None:
            return None

        return float(
            score
        )

    def lesson_score(
        self,
        user_id: str,
        exercise_ids: list[str],
    ) -> float | None:

        scores = []

        for exercise_id in (
            exercise_ids
        ):
            score = self.exercise_score(
                user_id,
                exercise_id,
            )

            if score is not None:
                scores.append(
                    score
                )

        if not scores:
            return None

        return float(
            mean(
                scores
            )
        )

    def passed(
        self,
        score: float | None,
    ) -> bool:

        if score is None:
            return False

        return (
            score
            >= self.PASS_SCORE
        )

    def mastered(
        self,
        score: float | None,
    ) -> bool:

        if score is None:
            return False

        return (
            score
            >= self.MASTERY_SCORE
        )

    def level_for_score(
        self,
        score: float | None,
    ) -> str:

        if score is None:
            return "not_started"

        if score < 50:
            return "needs_review"

        if score < self.PASS_SCORE:
            return "developing"

        if score < self.MASTERY_SCORE:
            return "passed"

        return "mastered"

    def summary(
        self,
        user_id: str,
    ):

        profile = (
            learning_profile_service
            .get(
                user_id
            )
        )

        if profile is None:
            return {
                "user_id": user_id,
                "average_score": None,
                "status": "not_started",
                "completed_exercises": 0,
            }

        values = [
            float(
                value
            )
            for value
            in profile.scores.values()
        ]

        average = (
            float(
                mean(
                    values
                )
            )
            if values
            else None
        )

        return {
            "user_id": user_id,
            "average_score": average,
            "status": (
                self.level_for_score(
                    average
                )
            ),
            "completed_exercises": len(
                profile.completed_exercises
            ),
        }


mastery_service = (
    MasteryService()
  )
