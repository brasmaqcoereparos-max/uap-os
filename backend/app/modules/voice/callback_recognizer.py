from __future__ import annotations

from collections.abc import Callable

from app.modules.voice.audio_buffer import (
    VoiceAudioBuffer,
)
from app.modules.voice.recognizer import (
    VoiceRecognizer,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


RecognizerCallback = Callable[
    [
        VoiceAudioBuffer,
        str,
    ],
    VoiceTranscript,
]


class VoiceCallbackRecognizer(
    VoiceRecognizer
):

    def __init__(
        self,
        name: str,
        callback: RecognizerCallback,
        available_callback: (
            Callable[[], bool]
            | None
        ) = None,
    ):
        normalized = str(
            name
        ).strip()

        if not normalized:
            raise ValueError(
                "Recognizer name "
                "cannot be empty"
            )

        if not callable(
            callback
        ):
            raise TypeError(
                "Recognizer callback "
                "must be callable"
            )

        if (
            available_callback
            is not None
            and not callable(
                available_callback
            )
        ):
            raise TypeError(
                "available_callback "
                "must be callable"
            )

        self._name = normalized
        self._callback = callback
        self._available_callback = (
            available_callback
        )

    @property
    def name(self) -> str:
        return self._name

    def available(self) -> bool:
        if (
            self._available_callback
            is None
        ):
            return True

        try:
            return bool(
                self._available_callback()
            )

        except Exception:
            return False

    def recognize(
        self,
        audio: VoiceAudioBuffer,
        language: str = "pt-BR",
    ) -> VoiceTranscript:
        if not self.available():
            raise RuntimeError(
                "Voice recognizer "
                f"'{self.name}' "
                "is not available"
            )

        result = self._callback(
            audio,
            language,
        )

        if not isinstance(
            result,
            VoiceTranscript,
        ):
            raise TypeError(
                "Recognizer callback "
                "must return VoiceTranscript"
            )

        result.metadata.setdefault(
            "recognizer",
            self.name,
        )

        return result
