from app.modules.ai.ui_assistant import (
    ai_ui_assistant,
)
from app.modules.ai.ui_intent import (
    AIUIIntent,
)


class AIUIAssistantService:

    def propose(
        self,
        text: str,
        app_type: str = "general",
        preferences: dict | None = None,
    ):
        intent = AIUIIntent(
            text=text,
            app_type=app_type,
            preferences=dict(
                preferences or {}
            ),
            confidence=1.0,
        )

        proposal = (
            ai_ui_assistant
            .propose(intent)
        )

        return {
            "intent": intent.to_dict(),
            "proposal": (
                proposal.to_dict()
            ),
            "target": "ui",
        }


ai_ui_assistant_service = (
    AIUIAssistantService()
)
