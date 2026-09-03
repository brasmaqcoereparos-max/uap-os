from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.voice.api_models import (
    VoiceSessionCreateRequest,
)
from app.modules.voice.service import (
    voice_service,
)


router = APIRouter()


@router.post("/sessions")
def create_session(
    data: VoiceSessionCreateRequest,
):
    session = (
        voice_service.create_session(
            language=data.language
        )
    )

    return session.to_dict()


@router.get("/sessions")
def list_sessions():
    return (
        voice_service.sessions()
    )


@router.get(
    "/sessions/{session_id}"
)
def get_session(
    session_id: str,
):
    session = (
        voice_service.get_session(
            session_id
        )
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice session not found"
            ),
        )

    return session.to_dict()


@router.delete(
    "/sessions/{session_id}"
)
def delete_session(
    session_id: str,
):
    session = (
        voice_service.remove_session(
            session_id
        )
    )

    if not session:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice session not found"
            ),
        )

    return {
        "deleted": True,
        "session_id": session_id,
    }
