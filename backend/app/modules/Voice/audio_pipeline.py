from app.modules.voice.audio_stream import (
    VoiceAudioStream,
)
from app.modules.voice.processor import (
    voice_processor,
)
from app.modules.voice.recognizer_manager import (
    voice_recognizer_manager,
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
    ):
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
            voice_processor.process(
                transcript=transcript,
                session=session,
            )
        )

        result[
            "audio"
        ] = stream.snapshot()

        return result


voice_audio_pipeline = (
    VoiceAudioPipeline()
      )
