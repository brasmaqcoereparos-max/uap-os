from __future__ import annotations

from app.modules.voice.audio_stream import (
    VoiceAudioStream,
)
from app.modules.voice.recognizer_manager import (
    voice_recognizer_manager,
)
from app.modules.voice.safe_pipeline import (
    voice_safe_pipeline,
)
from app.modules.voice.session import (
    VoiceSession,
)


class VoiceAudioPipeline:

    def process(
        self,
        stream: VoiceAudioStream,
        session: (
            VoiceSession | None
        ) = None,
        language: str = "pt-BR",
        recognizer_name: (
            str | None
        ) = None,
        tts_provider: (
            str | None
        ) = None,
    ):
        if not isinstance(
            stream,
            VoiceAudioStream,
        ):
            raise TypeError(
                "stream must be a "
                "VoiceAudioStream"
            )

        if not stream.buffer.size():
            raise ValueError(
                "Voice audio stream "
                "is empty"
            )

        transcript = (
            voice_recognizer_manager
            .recognize(
                audio=stream.buffer,
                language=language,
                recognizer_name=(
                    recognizer_name
                ),
            )
        )

        result = (
            voice_safe_pipeline
            .process_transcript(
                transcript=transcript,
                session=session,
                build_response=True,
                tts_provider=(
                    tts_provider
                ),
            )
        )

        result[
            "audio"
        ] = stream.snapshot()

        return result


voice_audio_pipeline = (
    VoiceAudioPipeline()
)
