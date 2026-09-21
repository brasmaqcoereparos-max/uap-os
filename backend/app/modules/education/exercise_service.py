from __future__ import annotations

from app.modules.education.schemas import (
    Exercise,
)


class ExerciseService:

    def __init__(self):
        self._exercises: dict[
            str,
            Exercise,
        ] = {}

    def register(
        self,
        exercise: Exercise,
    ):
        self._exercises[
            exercise.id
        ] = exercise

        return exercise

    def create(
        self,
        exercise_id: str,
        lesson_id: str,
        title: str,
        description: str = "",
        difficulty: str = "beginner",
        exercise_type: str = "practice",
        instructions=None,
        expected_result=None,
        metadata=None,
    ):
        if not exercise_id:
            raise ValueError(
                "exercise_id is required"
            )

        if not lesson_id:
            raise ValueError(
                "lesson_id is required"
            )

        exercise = Exercise(
            id=exercise_id,
            lesson_id=lesson_id,
            title=title,
            description=description,
            difficulty=difficulty,
            exercise_type=exercise_type,
            instructions=list(
                instructions or []
            ),
            expected_result=dict(
                expected_result or {}
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        return self.register(
            exercise
        )

    def get(
        self,
        exercise_id: str,
    ):
        return self._exercises.get(
            exercise_id
        )

    def require(
        self,
        exercise_id: str,
    ):
        exercise = self.get(
            exercise_id
        )

        if exercise is None:
            raise KeyError(
                "Exercise not found: "
                f"{exercise_id}"
            )

        return exercise

    def for_lesson(
        self,
        lesson_id: str,
    ):
        return [
            exercise
            for exercise
            in self._exercises.values()
            if exercise.lesson_id
            == lesson_id
        ]

    def complete(
        self,
        exercise_id: str,
    ):
        exercise = self.require(
            exercise_id
        )

        exercise.completed = True

        return exercise

    def reset(
        self,
        exercise_id: str,
    ):
        exercise = self.require(
            exercise_id
        )

        exercise.completed = False

        return exercise

    def list_all(self):
        return list(
            self._exercises.values()
        )

    def clear(self):
        self._exercises.clear()


exercise_service = ExerciseService()
