from fastapi import APIRouter

from app.modules.ai.api_models import (
    AIAutomationRequest,
)
from app.modules.ai.automation_assistant_service import (
    ai_automation_assistant_service,
)


router = APIRouter()


@router.post("/automation")
def automation_proposal(
    data: AIAutomationRequest,
):
    return (
        ai_automation_assistant_service
        .propose(
            text=data.text,
            objective=(
                data.objective
            ),
            entities=(
                data.entities
            ),
        )
    )
