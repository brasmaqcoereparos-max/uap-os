from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.security.security_session_manager import (
    security_session_manager,
)


router = APIRouter()


@router.post("/sessions")
def create_session(
    principal_id: str,
):
    session = (
        security_session_manager
        .create(
            principal_id=principal_id
        )
    )

    return session.to_dict()


@router.get("/sessions")
def list_sessions():
    return [
        session.to_dict()
        for session
        in security_session_manager
        .active()
    ]


@router.delete(
    "/sessions/{session_id}"
)
def close_session(
    session_id: str,
):
    closed = (
        security_session_manager
        .close(
            session_id
        )
    )

    if not closed:
        raise HTTPException(
            status_code=404,
            detail=(
                "Security session "
                "not found"
            ),
        )

    return {
        "closed": True,
        "session_id": session_id,
    }
