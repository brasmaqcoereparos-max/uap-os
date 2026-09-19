from __future__ import annotations

from app.modules.voice.audio_buffer import (
    VoiceAudioBuffer,
)
from app.modules.voice.recognizer import (
    VoiceRecognizer,
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
            if (
                voice_recognizer_registry
                .get(
                    voice_text_recognizer.name
                )
                is None
            ):
                voice_recognizer_registry.register(
                    voice_text_recognizer,
                    default=True,
                )

            self._initialized = True

        return self

    def register(
        self,
        recognizer: VoiceRecognizer,
        *,
        default: bool = False,
    ):
        self.initialize()

        if not isinstance(
            recognizer,
            VoiceRecognizer,
        ):
            raise TypeError(
                "recognizer must implement "
                "VoiceRecognizer"
            )

        return (
            voice_recognizer_registry
            .register(
                recognizer,
                default=default,
            )
        )

    def set_default(
        self,
        recognizer_name: str,
    ):
        self.initialize()

        return (
            voice_recognizer_registry
            .set_default(
                recognizer_name
            )
        )

    def recognize(
        self,
        audio: VoiceAudioBuffer,
        language: str = "pt-BR",
        recognizer_name: (
            str | None
        ) = None,
    ):
        self.initialize()

        if not isinstance(
            audio,
            VoiceAudioBuffer,
        ):
            raise TypeError(
                "audio must be a "
                "VoiceAudioBuffer"
            )

        if audio.size() <= 0:
            raise ValueError(
                "Voice audio buffer "
                "is empty"
            )

        if recognizer_name:
            recognizer = (
                voice_recognizer_registry
                .get(
                    recognizer_name
                )
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
                f"'{recognizer.name}' "
                "is not available"
            )

        transcript = (
            recognizer.recognize(
                audio=audio,
                language=language,
            )
        )

        if transcript is None:
            raise RuntimeError(
                "Voice recognizer returned "
                "no transcript"
            )

        transcript.metadata.setdefault(
            "recognizer",
            recognizer.name,
        )

        return transcript

    def recognizers(self):
        self.initialize()

        return [
            {
                "name": recognizer.name,
                "available": (
                    recognizer
                    .available()
                ),
                "default": (
                    voice_recognizer_registry
                    .default()
                    is recognizer
                ),
            }
            for recognizer
            in voice_recognizer_registry
            .list_all()
        ]


voice_recognizer_manager = (
    VoiceRecognizerManager()
)
