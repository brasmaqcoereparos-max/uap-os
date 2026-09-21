from __future__ import annotations

from app.modules.ai.education_assistant_service import (
    ai_education_assistant_service,
)
from app.modules.ai.learning_simulation_bridge import (
    ai_learning_simulation_bridge,
)


class EducationAITeacherBridge:

    def explain(
        self,
        *,
        topic: str,
        question: str = "",
        level: str = "beginner",
        context: dict | None = None,
    ):

        return (
            ai_education_assistant_service
            .explain(
                topic=topic,
                question=question,
                level=level,
                include_examples=True,
                include_exercises=True,
                context=context,
            )
        )

    def propose_exercise(
        self,
        *,
        topic: str,
        lesson_id: str,
        level: str = "beginner",
    ):

        return (
            ai_education_assistant_service
            .propose_exercise(
                topic=topic,
                lesson_id=lesson_id,
                level=level,
            )
        )

    def propose_lab(
        self,
        *,
        topic: str,
        level: str = "beginner",
    ):

        return (
            ai_learning_simulation_bridge
            .propose_lab(
                topic=topic,
                level=level,
            )
        )


education_ai_teacher_bridge = (
    EducationAITeacherBridge()
)
