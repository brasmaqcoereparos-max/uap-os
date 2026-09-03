from app.modules.voice.interaction_service import (
    voice_interaction_service,
)
from app.modules.voice.service import (
    voice_service,
)
from app.modules.voice.voice_health import (
    voice_health,
)


class VoiceFacade:

    def create_session(
        self,
        language: str = "pt-BR",
    ):
        return (
            voice_service
            .create_session(
                language=language
            )
        )

    def process_text(
        self,
        session_id: str,
        text: str,
    ):
        return (
            voice_interaction_service
            .process_text(
                session_id=session_id,
                text=text,
            )
        )

    def health(self):
        return voice_health.check()

    def sessions(self):
        return voice_service.sessions()


voice_facade = VoiceFacade()
