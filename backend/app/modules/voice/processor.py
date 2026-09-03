from app.modules.voice.command_mapper import (
    voice_command_mapper,
)
from app.modules.voice.enums import (
    VoiceInputState,
)
from app.modules.voice.intent_resolver import (
    voice_intent_resolver,
)
from app.modules.voice.session import (
    VoiceSession,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceProcessor:

    def process(
        self,
        transcript: VoiceTranscript,
        session: (
            VoiceSession | None
        ) = None,
    ):
        if session is None:
            session = VoiceSession(
                language=(
                    transcript.language
                )
            )

        session.set_state(
            VoiceInputState.PROCESSING
        )

        if transcript.is_empty():
            session.set_state(
                VoiceInputState.ERROR
            )

            return {
                "session": (
                    session.to_dict()
                ),
                "transcript": (
                    transcript.to_dict()
                ),
                "intent": None,
                "command": None,
                "error": (
                    "Empty transcript"
                ),
            }

        intent = (
            voice_intent_resolver
            .resolve(transcript)
        )

        command = (
            voice_command_mapper
            .map(intent)
        )

        session.set_state(
            VoiceInputState.READY
        )

        return {
            "session": (
                session.to_dict()
            ),
            "transcript": (
                transcript.to_dict()
            ),
            "intent": (
                intent.to_dict()
            ),
            "command": (
                command.to_dict()
                if command
                else None
            ),
            "error": None,
        }


voice_processor = (
    VoiceProcessor()
      )
