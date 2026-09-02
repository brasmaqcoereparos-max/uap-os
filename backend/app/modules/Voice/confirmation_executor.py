from app.modules.voice.confirmation_manager import (
    voice_confirmation_manager,
)
from app.modules.voice.executor import (
    voice_executor,
)


class VoiceConfirmationExecutor:

    def execute(
        self,
        confirmation_id: str,
    ):
        confirmation = (
            voice_confirmation_manager
            .get(
                confirmation_id
            )
        )

        if not confirmation:
            raise ValueError(
                "Voice confirmation "
                "not found"
            )

        if not confirmation.confirmed:
            raise ValueError(
                "Voice confirmation "
                "has not been confirmed"
            )

        result = (
            voice_executor.execute(
                confirmation.command
            )
        )

        voice_confirmation_manager.remove(
            confirmation_id
        )

        return result


voice_confirmation_executor = (
    VoiceConfirmationExecutor()
  )
