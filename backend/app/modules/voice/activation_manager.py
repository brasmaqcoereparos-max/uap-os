from datetime import datetime
from datetime import timedelta
from datetime import timezone

from app.modules.voice.activation_state import (
    VoiceActivationState,
)


class VoiceActivationManager:

    def __init__(
        self,
        timeout_seconds: int = 15,
    ):
        self.timeout_seconds = max(
            1,
            int(timeout_seconds),
        )

        self._states: dict[
            str,
            VoiceActivationState,
        ] = {}

    def state(
        self,
        session_id: str,
    ):
        return self._states.setdefault(
            session_id,
            VoiceActivationState(),
        )

    def activate(
        self,
        session_id: str,
    ):
        expires_at = (
            datetime.now(
                timezone.utc
            )
            + timedelta(
                seconds=(
                    self.timeout_seconds
                )
            )
        )

        state = self.state(
            session_id
        )

        state.activate(
            expires_at=expires_at
        )

        return state

    def deactivate(
        self,
        session_id: str,
    ):
        state = self.state(
            session_id
        )

        state.deactivate()

        return state

    def is_active(
        self,
        session_id: str,
    ):
        state = self.state(
            session_id
        )

        if not state.active:
            return False

        if (
            state.expires_at
            is not None
            and datetime.now(
                timezone.utc
            ) >= state.expires_at
        ):
            state.deactivate()

            return False

        return True


voice_activation_manager = (
    VoiceActivationManager()
          )
