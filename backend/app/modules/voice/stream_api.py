from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import WebSocket

from app.modules.voice.api_models import (
    VoiceStreamChunkRequest,
    VoiceStreamProcessRequest,
)
from app.modules.voice.audio_codec import (
    voice_audio_codec,
)
from app.modules.voice.audio_stream_manager import (
    voice_audio_stream_manager,
)
from app.modules.voice.voice_input import (
    voice_input,
)


router = APIRouter()


@router.post("/streams")
def create_stream():
    stream = voice_input.create_stream()

    return stream.snapshot()


@router.get("/streams")
def list_streams():
    return (
        voice_audio_stream_manager
        .list_all()
    )


@router.post(
    "/streams/{stream_id}/chunk"
)
def push_chunk(
    stream_id: str,
    data: VoiceStreamChunkRequest,
):
    try:
        chunk_data = (
            voice_audio_codec
            .decode_base64(
                data.data
            )
        )

        return voice_input.push(
            stream_id=stream_id,
            data=chunk_data,
            sequence=data.sequence,
            final=data.final,
            sample_rate=(
                data.sample_rate
            ),
            channels=data.channels,
            sample_width=(
                data.sample_width
            ),
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.post(
    "/streams/{stream_id}/process"
)
def process_stream(
    stream_id: str,
    data: VoiceStreamProcessRequest,
):
    try:
        return voice_input.process(
            stream_id=stream_id,
            session_id=data.session_id,
            language=data.language,
            recognizer_name=(
                data.recognizer_name
            ),
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc
