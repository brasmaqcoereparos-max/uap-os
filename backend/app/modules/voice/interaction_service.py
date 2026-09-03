from app.modules.voice.interaction_controller import (
    voice_interaction_controller,
)
from app.modules.voice.safe_pipeline import (
    voice_safe_pipeline,
)
from app.modules.voice.service import (
    voice_service,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceInteractionService:

    def process_text(
        self,
        session_id: str,
        text: str,
    ):
        session = (
            voice_service.get_session(
                session_id
            )
        )

        if not session:
            raise ValueError(
                "Voice session not found"
            )

        prepared = (
            voice_interaction_controller
            .prepare_text(
                session_id,
                text,
            )
        )

        if not prepared[
            "accepted"
        ]:
            return {
                "interaction": (
                    prepared
                ),
                "result": None,
            }

        transcript = VoiceTranscript(
            text=prepared["text"],
            language=session.language,
            final=True,
        )

        result = (
            voice_safe_pipeline
            .process_transcript(
                transcript=transcript,
                session=session,
            )
        )

        return {
            "interaction": prepared,
            "result": result,
        }


voice_interaction_service = (
    VoiceInteractionService()
)
