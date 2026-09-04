from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.ai.assistant_facade import (
    ai_assistant_facade,
)


router = APIRouter()


@router.post("/sessions")
def create_session(
    user_id: str | None = None,
    project_id: str | None = None,
    user_level: str | None = None,
):
    return (
        ai_assistant_facade
        .create_session(
            user_id=user_id,
            project_id=project_id,
            user_level=user_level,
        )
    )


@router.post("/sessions/{session_id}/ask")
def ask_session(
    session_id: str,
    text: str,
    provider_name: str | None = None,
    model: str | None = None,
):
    try:
        response = (
            ai_assistant_facade
            .ask(
                session_id=session_id,
                text=text,
                provider_name=provider_name,
                model=model,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return response.to_dict()
