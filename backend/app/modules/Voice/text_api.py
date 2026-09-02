from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.voice.api_models import (
    VoiceTextRequest,
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


router = APIRouter()


@router.post("/text")
def process_text(
    data: VoiceTextRequest,
):
    session = None

    if data.session_id:
        session = (
            voice_service.get_session(
                data.session_id
            )
        )

        if not session:
            raise HTTPException(
                status_code=404,
                detail=(
                    "Voice session "
                    "not found"
                ),
            )

    transcript = VoiceTranscript(
        text=data.text,
        language=data.language,
        confidence=data.confidence,
        final=True,
    )

    return (
        voice_safe_pipeline
        .process_transcript(
            transcript=transcript,
            session=session,
        )
  )
