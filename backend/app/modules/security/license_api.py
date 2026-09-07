from fastapi import APIRouter

from app.modules.security.api_models import (
    SecurityLicenseValidateRequest,
)
from app.modules.security.license_service import (
    license_service,
)


router = APIRouter()


@router.post("/license/validate")
def validate_license(
    data: (
        SecurityLicenseValidateRequest
    ),
):
    return (
        license_service
        .validate_device(
            data.device_id
        )
    )


@router.get("/licenses")
def list_licenses():
    return (
        license_service
        .list_all()
    )
