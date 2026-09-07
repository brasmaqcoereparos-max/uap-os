from fastapi import APIRouter

from app.modules.security.module_access_service import (
    security_module_access_service,
)


router = APIRouter()


@router.get(
    "/modules/{module}/access"
)
def check_module_access(
    module: str,
    device_id: str,
):
    return (
        security_module_access_service
        .check(
            device_id=device_id,
            module=module,
        )
    )
