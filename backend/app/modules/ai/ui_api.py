from fastapi import APIRouter

from app.modules.ai.api_models import (
    AIUIRequest,
)
from app.modules.ai.ui_assistant_service import (
    ai_ui_assistant_service,
)


router = APIRouter()


@router.post("/ui")
def ui_proposal(
    data: AIUIRequest,
):
    return (
        ai_ui_assistant_service
        .propose(
            text=data.text,
            app_type=(
                data.app_type
            ),
            preferences=(
                data.preferences
            ),
        )
    )
