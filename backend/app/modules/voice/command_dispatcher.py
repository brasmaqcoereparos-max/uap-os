from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.command_validator import (
    voice_command_validator,
)
from app.modules.voice.confirmation_manager import (
    voice_confirmation_manager,
)
from app.modules.voice.dispatch_result import (
    VoiceDispatchResult,
)


class VoiceCommandDispatcher:

    def dispatch(
        self,
        command: VoiceCommand,
    ):
        validation = (
            voice_command_validator
            .validate(command)
        )

        if not validation.valid:
            return VoiceDispatchResult(
                accepted=False,
                status="rejected",
                command=(
                    command.to_dict()
                ),
                errors=list(
                    validation.errors
                ),
            )

        if (
            validation
            .requires_confirmation
        ):
            confirmation = (
                voice_confirmation_manager
                .create(command)
            )

            return VoiceDispatchResult(
                accepted=True,
                status=(
                    "confirmation_required"
                ),
                command=(
                    command.to_dict()
                ),
                confirmation_id=(
                    confirmation.id
                ),
            )

        return VoiceDispatchResult(
            accepted=True,
            status="ready",
            command=command.to_dict(),
        )


voice_command_dispatcher = (
    VoiceCommandDispatcher()
          )
