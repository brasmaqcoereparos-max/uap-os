from fastapi import APIRouter

from app.modules.security.activation_request import (
    OfflineActivationRequest,
)
from app.modules.security.api_models import (
    SecurityOfflineActivationRequest,
)
from app.modules.security.offline_activation import (
    offline_activation_service,
)


router = APIRouter()


@router.post("/activation/offline")
def create_offline_activation(
    data: (
        SecurityOfflineActivationRequest
    ),
):
    request = (
        OfflineActivationRequest(
            device_id=data.device_id,
            hardware_id=(
                data.hardware_id
            ),
            product=data.product,
            metadata=dict(
                data.metadata
            ),
        )
    )

    code = (
        offline_activation_service
        .generate_code(
            request=request,
            license_id=(
                data.license_id
            ),
            secret=data.secret,
            key_id=data.key_id,
        )
    )

    return code.to_dict()
