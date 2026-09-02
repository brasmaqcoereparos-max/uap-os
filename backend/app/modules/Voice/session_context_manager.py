from app.modules.voice.session_context import (
    VoiceSessionContext,
)


class VoiceSessionContextManager:

    def __init__(self):
        self._contexts: dict[
            str,
            VoiceSessionContext,
        ] = {}

    def get(
        self,
        session_id: str,
    ):
        return self._contexts.get(
            session_id
        )

    def get_or_create(
        self,
        session_id: str,
    ):
        context = self.get(
            session_id
        )

        if context:
            return context

        context = VoiceSessionContext(
            session_id=session_id
        )

        self._contexts[
            session_id
        ] = context

        return context

    def remove(
        self,
        session_id: str,
    ):
        return self._contexts.pop(
            session_id,
            None,
        )

    def clear(self):
        self._contexts.clear()


voice_session_context_manager = (
    VoiceSessionContextManager()
  )
