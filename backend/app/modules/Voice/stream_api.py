from fastapi import APIRouter
from fastapi import HTTPException

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
    stream = (
        voice_input.create_stream()
    )

    return stream.snapshot()


@router.get("/streams")
def list_streams():
    return (
        voice_audio_stream_manager
        .list_all()
    )


@router.get(
    "/streams/{stream_id}"
)
def get_stream(
    stream_id: str,
):
    stream = (
        voice_audio_stream_manager
        .get(stream_id)
    )

    if not stream:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice audio stream "
                "not found"
            ),
        )

    return stream.snapshot()


@router.post(
    "/streams/{stream_id}/chunks"
)
def push_chunk(
    stream_id: str,
    data: VoiceStreamChunkRequest,
):
    try:
        raw = (
            voice_audio_codec
            .decode_base64(
                data.data
            )
        )

        return voice_input.push(
            stream_id=stream_id,
            data=raw,
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
            session_id=(
                data.session_id
            ),
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


@router.delete(
    "/streams/{stream_id}"
)
def delete_stream(
    stream_id: str,
):
    stream = (
        voice_audio_stream_manager
        .remove(stream_id)
    )

    if not stream:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice audio stream "
                "not found"
            ),
        )

    return {
        "deleted": True,
        "stream_id": stream_id,
}
