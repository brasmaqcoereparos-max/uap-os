from fastapi import APIRouter

from app.modules.ai.api_models import (
    AIHardwareRequest,
)
from app.modules.ai.hardware_assistant_service import (
    ai_hardware_assistant_service,
)


router = APIRouter()


@router.post("/hardware")
def recommend_hardware(
    data: AIHardwareRequest,
):
    return (
        ai_hardware_assistant_service
        .recommend(
            requirements=(
                data.requirements
            ),
            boards=data.boards,
        )
    )
