from fastapi import APIRouter

from app.modules.security.runtime_security_service import (
    runtime_security_service,
)


router = APIRouter()


@router.get(
    "/runtime/access"
)
def runtime_access(
    device_id: str,
):
    result = (
        runtime_security_service
        .authorize(
            device_id=device_id
        )
    )

    return result.to_dict()
