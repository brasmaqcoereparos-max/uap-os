from fastapi import APIRouter

from app.modules.voice.api_models import (
    VoiceCommandValidateRequest,
)
from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.command_dispatcher import (
    voice_command_dispatcher,
)
from app.modules.voice.command_validator import (
    voice_command_validator,
)


router = APIRouter()


def _command(
    data: VoiceCommandValidateRequest,
):
    return VoiceCommand(
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


@router.post(
    "/commands/validate"
)
def validate_command(
    data: VoiceCommandValidateRequest,
):
    command = _command(data)

    return (
        voice_command_validator
        .validate(command)
        .to_dict()
    )


@router.post(
    "/commands/dispatch"
)
def dispatch_command(
    data: VoiceCommandValidateRequest,
):
    command = _command(data)

    return (
        voice_command_dispatcher
        .dispatch(command)
        .to_dict()
    )
