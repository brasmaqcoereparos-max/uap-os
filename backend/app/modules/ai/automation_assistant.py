from app.modules.ai.automation_intent import (
    AIAutomationIntent,
)
from app.modules.ai.automation_proposal import (
    AIAutomationProposal,
)


class AIAutomationAssistant:

    def propose(
        self,
        intent: AIAutomationIntent,
    ):
        proposal = AIAutomationProposal(
            name=(
                intent.objective
                or "Automation"
            ),
            description=intent.text,
        )

        proposal.triggers.append(
            {
                "type": "manual",
                "source": "application",
            }
        )

        proposal.actions.append(
            {
                "type": "proposal",
                "target": "automation",
                "parameters": dict(
                    intent.entities
                ),
            }
        )

        return proposal


ai_automation_assistant = (
    AIAutomationAssistant()
)
