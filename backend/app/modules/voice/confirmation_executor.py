from __future__ import annotations

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
            voice_confirmation_manager.get(
                confirmation_id
            )
        )

        if confirmation is None:
            raise ValueError(
                "Voice confirmation not found"
            )

        if confirmation.cancelled:
            raise ValueError(
                "Voice confirmation was cancelled"
            )

        if not confirmation.confirmed:
            raise ValueError(
                "Voice confirmation is not confirmed"
            )

        execution = voice_executor.execute(
            confirmation.command
        )

        if execution.executed:
            voice_confirmation_manager.remove(
                confirmation_id
            )

        return execution


voice_confirmation_executor = (
    VoiceConfirmationExecutor()
)
