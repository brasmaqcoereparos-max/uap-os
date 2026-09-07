from fastapi import APIRouter

from app.modules.security.security_boundary_service import (
    security_boundary_service,
)


router = APIRouter()


@router.get(
    "/boundary/module/{module}"
)
def check_module_boundary(
    module: str,
    device_id: str,
):
    return (
        security_boundary_service
        .check_module(
            device_id=device_id,
            module=module,
        )
    )


@router.get(
    "/boundary/runtime"
)
def check_runtime_boundary(
    device_id: str,
):
    return (
        security_boundary_service
        .check_runtime(
            device_id=device_id
        )
    )
