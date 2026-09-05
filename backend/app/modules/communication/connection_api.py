from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.communication.api_models import (
    CommunicationConnectionRequest,
    CommunicationSendRequest,
)
from app.modules.communication.connection_manager import (
    communication_connection_manager,
)
from app.modules.communication.connection_service import (
    communication_connection_service,
)


router = APIRouter()


@router.post("/connections")
def open_connection(
    data: CommunicationConnectionRequest,
):
    try:
        return (
            communication_connection_service
            .open(
                transport=(
                    data.transport
                ),
                destination=(
                    data.destination
                ),
            )
        )

    except (
        ValueError,
        RuntimeError,
    ) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.get("/connections")
def list_connections():
    return [
        connection.to_dict()
        for connection
        in communication_connection_manager
        .list_all()
    ]


@router.post(
    "/connections/"
    "{connection_id}/send"
)
def send(
    connection_id: str,
    data: CommunicationSendRequest,
):
    try:
        return (
            communication_connection_service
            .send(
                connection_id=(
                    connection_id
                ),
                payload=data.payload,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.delete(
    "/connections/"
    "{connection_id}"
)
def close_connection(
    connection_id: str,
):
    result = (
        communication_connection_service
        .close(
            connection_id
        )
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail=(
                "Communication "
                "connection not found"
            ),
        )

    return {
        "closed": True,
        "connection_id": (
            connection_id
        ),
              }
