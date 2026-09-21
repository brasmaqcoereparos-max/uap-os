from __future__ import annotations

from typing import Any

from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.schemas import (
    AssessmentResult,
)


class AssessmentService:

    def assess(
        self,
        exercise_id: str,
        answer: dict[str, Any],
    ):
        exercise = (
            exercise_service.require(
                exercise_id
            )
        )

        expected = dict(
            exercise.expected_result
        )

        if not expected:
            return AssessmentResult(
                exercise_id=(
                    exercise_id
                ),
                passed=True,
                score=100.0,
                feedback=[
                    (
                        "Exercise completed. "
                        "Manual review may be "
                        "required."
                    )
                ],
            )

        total = len(
            expected
        )

        correct = 0

        errors = []

        for (
            key,
            expected_value,
        ) in expected.items():

            received = answer.get(
                key
            )

            if (
                received
                == expected_value
            ):
                correct += 1

            else:
                errors.append(
                    (
                        f"{key}: expected "
                        f"{expected_value}, "
                        f"received {received}"
                    )
                )

        score = (
            correct
            / total
            * 100.0
            if total
            else 100.0
        )

        passed = (
            score >= 70.0
        )

        feedback = []

        if passed:
            feedback.append(
                "Exercise passed."
            )

        else:
            feedback.append(
                "Review the incorrect "
                "items and try again."
            )

        return AssessmentResult(
            exercise_id=exercise_id,
            passed=passed,
            score=score,
            feedback=feedback,
            errors=errors,
        )


assessment_service = (
    AssessmentService()
)
