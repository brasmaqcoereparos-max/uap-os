from fastapi import APIRouter

from app.modules.communication.api_models import (
    CommunicationPublishRequest,
)
from app.modules.communication.communication_facade import (
    communication_facade,
)


router = APIRouter()


@router.post("/publish")
def publish(
    data: CommunicationPublishRequest,
):
    result = (
        communication_facade
        .publish(
            topic=data.topic,
            source=data.source,
            payload=data.payload,
            target=data.target,
        )
    )

    return result.to_dict()
