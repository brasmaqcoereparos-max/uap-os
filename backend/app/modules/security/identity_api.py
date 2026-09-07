from fastapi import APIRouter

from app.modules.security.api_models import (
    SecurityIdentityRequest,
)
from app.modules.security.security_facade import (
    security_facade,
)


router = APIRouter()


@router.post("/identity")
def identify_device(
    data: SecurityIdentityRequest,
):
    return (
        security_facade
        .identify_device(
            serial_number=(
                data.serial_number
            ),
            board=data.board,
            model=data.model,
        )
    )
