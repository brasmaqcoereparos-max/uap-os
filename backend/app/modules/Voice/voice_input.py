from app.modules.voice.audio_chunk import (
    VoiceAudioChunk,
)
from app.modules.voice.audio_pipeline import (
    voice_audio_pipeline,
)
from app.modules.voice.audio_stream_manager import (
    voice_audio_stream_manager,
)
from app.modules.voice.service import (
    voice_service,
)


class VoiceInput:

    def create_stream(self):
        return (
            voice_audio_stream_manager
            .create()
        )

    def push(
        self,
        stream_id: str,
        data: bytes,
        sequence: int = 0,
        final: bool = False,
        sample_rate: int = 16000,
        channels: int = 1,
        sample_width: int = 2,
    ):
        stream = (
            voice_audio_stream_manager
            .get(stream_id)
        )

        if not stream:
            raise ValueError(
                "Voice audio stream "
                "not found"
            )

        chunk = VoiceAudioChunk(
            data=data,
            sequence=sequence,
            final=final,
            sample_rate=sample_rate,
            channels=channels,
            sample_width=sample_width,
        )

        stream.write(chunk)

        return stream.snapshot()

    def process(
        self,
        stream_id: str,
        session_id: (
            str | None
        ) = None,
        language: str = "pt-BR",
        recognizer_name: (
            str | None
        ) = None,
    ):
        stream = (
            voice_audio_stream_manager
            .get(stream_id)
        )

        if not stream:
            raise ValueError(
                "Voice audio stream "
                "not found"
            )

        session = None

        if session_id:
            session = (
                voice_service
                .get_session(
                    session_id
                )
            )

            if not session:
                raise ValueError(
                    "Voice session "
                    "not found"
                )

        return (
            voice_audio_pipeline
            .process(
                stream=stream,
                session=session,
                language=language,
                recognizer_name=(
                    recognizer_name
                ),
            )
        )


voice_input = VoiceInput()
