from fastapi import APIRouter

from app.modules.security.api_models import (
    SecuritySignLicenseRequest,
)
from app.modules.security.license_payload import (
    LicensePayload,
)
from app.modules.security.license_signer import (
    license_signer,
)


router = APIRouter()


@router.post("/license/sign")
def sign_license(
    data: (
        SecuritySignLicenseRequest
    ),
):
    payload = (
        LicensePayload(
            license_id=(
                data.payload
                .license_id
            ),
            device_id=(
                data.payload
                .device_id
            ),
            product=(
                data.payload
                .product
            ),
            issued_at=(
                data.payload
                .issued_at
            ),
            expires_at=(
                data.payload
                .expires_at
            ),
            features=list(
                data.payload
                .features
            ),
            metadata=dict(
                data.payload
                .metadata
            ),
        )
    )

    signed = (
        license_signer
        .sign(
            payload=payload,
            secret=data.secret,
            key_id=data.key_id,
        )
    )

    return signed.to_dict()
