from fastapi import APIRouter

from app.modules.ai.api_models import (
    AIPlanRequest,
)
from app.modules.ai.planner_service import (
    ai_planner_service,
)


router = APIRouter()


@router.post("/plan")
def create_plan(
    data: AIPlanRequest,
):
    return (
        ai_planner_service
        .plan(
            title=data.title,
            description=(
                data.description
            ),
            task_type=(
                data.task_type
            ),
            parameters=(
                data.parameters
            ),
        )
    )
