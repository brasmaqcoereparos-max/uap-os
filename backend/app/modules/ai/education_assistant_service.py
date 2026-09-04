from app.modules.ai.education_assistant import (
    ai_education_assistant,
)
from app.modules.ai.education_profile import (
    AIEducationProfile,
)
from app.modules.ai.education_request import (
    AIEducationRequest,
)


class AIEducationAssistantService:

    def explain(
        self,
        topic: str,
        question: str = "",
        level: str = "beginner",
        language: str = "pt-BR",
        include_examples: bool = True,
        include_exercises: bool = False,
        context: dict | None = None,
    ):
        profile = AIEducationProfile(
            level=level,
            language=language,
            step_by_step=True,
            include_examples=(
                include_examples
            ),
            include_exercises=(
                include_exercises
            ),
        )

        request = AIEducationRequest(
            topic=topic,
            question=question,
            profile=profile,
            context=dict(
                context or {}
            ),
        )

        response = (
            ai_education_assistant
            .explain(request)
        )

        return {
            "request": (
                request.to_dict()
            ),
            "response": (
                response.to_dict()
            ),
            "target": "education",
        }


ai_education_assistant_service = (
    AIEducationAssistantService()
      )
