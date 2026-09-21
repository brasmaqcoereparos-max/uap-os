from __future__ import annotations

from app.modules.education.schemas import (
    Lesson,
)


class LessonService:

    VALID_LEVELS = {
        "beginner",
        "intermediate",
        "professional",
    }

    def __init__(self):
        self._lessons: dict[
            str,
            Lesson,
        ] = {}

    def register(
        self,
        lesson: Lesson,
    ):
        if (
            lesson.difficulty
            not in self.VALID_LEVELS
        ):
            raise ValueError(
                "Invalid lesson difficulty: "
                f"{lesson.difficulty}"
            )

        self._lessons[
            lesson.id
        ] = lesson

        return lesson

    def create(
        self,
        lesson_id: str,
        title: str,
        description: str,
        difficulty: str = "beginner",
        objectives=None,
        content=None,
        prerequisites=None,
        metadata=None,
    ):
        if not lesson_id:
            raise ValueError(
                "lesson_id is required"
            )

        if not title:
            raise ValueError(
                "Lesson title is required"
            )

        lesson = Lesson(
            id=lesson_id,
            title=title,
            description=description,
            difficulty=difficulty,
            objectives=list(
                objectives or []
            ),
            content=list(
                content or []
            ),
            prerequisites=list(
                prerequisites or []
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        return self.register(
            lesson
        )

    def get(
        self,
        lesson_id: str,
    ):
        return self._lessons.get(
            lesson_id
        )

    def require(
        self,
        lesson_id: str,
    ):
        lesson = self.get(
            lesson_id
        )

        if lesson is None:
            raise KeyError(
                "Lesson not found: "
                f"{lesson_id}"
            )

        return lesson

    def list_all(
        self,
        difficulty: str | None = None,
    ):
        lessons = list(
            self._lessons.values()
        )

        if difficulty:
            lessons = [
                lesson
                for lesson in lessons
                if lesson.difficulty
                == difficulty
            ]

        return lessons

    def remove(
        self,
        lesson_id: str,
    ):
        return self._lessons.pop(
            lesson_id,
            None,
        )

    def clear(self):
        self._lessons.clear()


lesson_service = LessonService()
