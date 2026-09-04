from fastapi import APIRouter

from app.modules.ai.api_models import (
    AIProjectRequest,
)
from app.modules.ai.project_builder_service import (
    ai_project_builder_service,
)


router = APIRouter()


@router.post("/project")
def build_project(
    data: AIProjectRequest,
):
    result = (
        ai_project_builder_service
        .create(
            name=data.name,
            objective=data.objective,
            requirements=(
                data.requirements
            ),
        )
    )

    return result.to_dict()
