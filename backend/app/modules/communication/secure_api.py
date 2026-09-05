from fastapi import APIRouter

from app.modules.communication.api_models import (
    SecureCommunicationPublishRequest,
)
from app.modules.communication.auth_context import (
    CommunicationAuthContext,
)
from app.modules.communication.secure_message_bus import (
    secure_communication_message_bus,
)


router = APIRouter()


@router.post("/secure/publish")
def secure_publish(
    data: (
        SecureCommunicationPublishRequest
    ),
):
    auth_context = None

    if data.auth:
        auth_context = (
            CommunicationAuthContext(
                principal_id=(
                    data.auth
                    .principal_id
                ),
                authenticated=(
                    data.auth
                    .authenticated
                ),
                roles=set(
                    data.auth.roles
                ),
                permissions=set(
                    data.auth
                    .permissions
                ),
            )
        )

    return (
        secure_communication_message_bus
        .publish(
            topic=data.topic,
            source=data.source,
            payload=data.payload,
            target=data.target,
            auth_context=(
                auth_context
            ),
        )
    )
