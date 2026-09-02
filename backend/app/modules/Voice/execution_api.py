from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.voice.api_models import (
    VoiceCommandValidateRequest,
)
from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.dispatch_executor import (
    voice_dispatch_executor,
)


router = APIRouter()


@router.post(
    "/commands/execute"
)
def execute_command(
    data: VoiceCommandValidateRequest,
):
    command = VoiceCommand(
        command=data.command,
        parameters=dict(
            data.parameters
        ),
        source=data.source,
        confidence=data.confidence,
        requires_confirmation=(
            data.requires_confirmation
        ),
    )

    return (
        voice_dispatch_executor
        .dispatch_and_execute(
            command
        )
    )


@router.post(
    "/confirmations/"
    "{confirmation_id}/execute"
)
def execute_confirmation(
    confirmation_id: str,
):
    try:
        return (
            voice_dispatch_executor
            .execute_confirmed(
                confirmation_id
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
