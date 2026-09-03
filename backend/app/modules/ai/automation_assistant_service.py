from app.modules.ai.automation_assistant import (
    ai_automation_assistant,
)
from app.modules.ai.automation_intent import (
    AIAutomationIntent,
)


class AIAutomationAssistantService:

    def propose(
        self,
        text: str,
        objective: str = "",
        entities: dict | None = None,
    ):
        intent = AIAutomationIntent(
            text=text,
            objective=objective,
            entities=dict(
                entities or {}
            ),
            confidence=1.0,
        )

        proposal = (
            ai_automation_assistant
            .propose(intent)
        )

        return {
            "intent": intent.to_dict(),
            "proposal": (
                proposal.to_dict()
            ),
            "direct_hardware": False,
        }


ai_automation_assistant_service = (
    AIAutomationAssistantService()
)
