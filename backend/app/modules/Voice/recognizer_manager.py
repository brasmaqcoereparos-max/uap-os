from app.modules.voice.audio_buffer import (
    VoiceAudioBuffer,
)
from app.modules.voice.recognizer_registry import (
    voice_recognizer_registry,
)
from app.modules.voice.text_recognizer import (
    voice_text_recognizer,
)


class VoiceRecognizerManager:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            voice_recognizer_registry.register(
                voice_text_recognizer,
                default=True,
            )

            self._initialized = True

        return self

    def recognize(
        self,
        audio: VoiceAudioBuffer,
        language: str = "pt-BR",
        recognizer_name: (
            str | None
        ) = None,
    ):
        self.initialize()

        if recognizer_name:
            recognizer = (
                voice_recognizer_registry
                .get(recognizer_name)
            )
        else:
            recognizer = (
                voice_recognizer_registry
                .default()
            )

        if not recognizer:
            raise ValueError(
                "Voice recognizer "
                "not found"
            )

        if not recognizer.available():
            raise RuntimeError(
                "Voice recognizer "
                "is not available"
            )

        return recognizer.recognize(
            audio=audio,
            language=language,
        )

    def recognizers(self):
        self.initialize()

        return [
            {
                "name": recognizer.name,
                "available": (
                    recognizer
                    .available()
                ),
            }
            for recognizer
            in voice_recognizer_registry
            .list_all()
        ]


voice_recognizer_manager = (
    VoiceRecognizerManager()
)
