from app.modules.voice.processor import (
    voice_processor,
)
from app.modules.voice.session import (
    VoiceSession,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceService:

    def __init__(self):
        self._sessions: dict[
            str,
            VoiceSession,
        ] = {}

    def create_session(
        self,
        language: str = "pt-BR",
    ):
        session = VoiceSession(
            language=language
        )

        self._sessions[
            session.id
        ] = session

        return session

    def get_session(
        self,
        session_id: str,
    ):
        return self._sessions.get(
            session_id
        )

    def remove_session(
        self,
        session_id: str,
    ):
        return self._sessions.pop(
            session_id,
            None,
        )

    def process_text(
        self,
        text: str,
        language: str = "pt-BR",
        confidence: (
            float | None
        ) = None,
        session_id: (
            str | None
        ) = None,
    ):
        session = None

        if session_id:
            session = self.get_session(
                session_id
            )

            if not session:
                raise ValueError(
                    "Voice session "
                    "not found"
                )

        transcript = VoiceTranscript(
            text=text,
            language=language,
            confidence=confidence,
            final=True,
        )

        return (
            voice_processor.process(
                transcript=transcript,
                session=session,
            )
        )

    def sessions(self):
        return [
            session.to_dict()
            for session
            in self._sessions.values()
        ]


voice_service = VoiceService()
