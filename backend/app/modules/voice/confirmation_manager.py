from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.confirmation import (
    VoiceConfirmation,
)


class VoiceConfirmationManager:

    def __init__(self):
        self._pending: dict[
            str,
            VoiceConfirmation,
        ] = {}

    def create(
        self,
        command: VoiceCommand,
    ):
        confirmation = (
            VoiceConfirmation(
                command=command
            )
        )

        self._pending[
            confirmation.id
        ] = confirmation

        return confirmation

    def get(
        self,
        confirmation_id: str,
    ):
        return self._pending.get(
            confirmation_id
        )

    def confirm(
        self,
        confirmation_id: str,
    ):
        confirmation = self.get(
            confirmation_id
        )

        if not confirmation:
            return None

        confirmation.confirm()

        return confirmation

    def cancel(
        self,
        confirmation_id: str,
    ):
        confirmation = self.get(
            confirmation_id
        )

        if not confirmation:
            return None

        confirmation.cancel()

        return confirmation

    def remove(
        self,
        confirmation_id: str,
    ):
        return self._pending.pop(
            confirmation_id,
            None,
        )

    def pending(self):
        return [
            confirmation
            for confirmation
            in self._pending.values()
            if confirmation.pending()
        ]


voice_confirmation_manager = (
    VoiceConfirmationManager()
)
