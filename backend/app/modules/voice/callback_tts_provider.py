from __future__ import annotations

from collections.abc import Callable

from app.modules.voice.tts_provider import (
    VoiceTTSProvider,
)
from app.modules.voice.tts_result import (
    VoiceTTSResult,
)


TTSCallback = Callable[
    [
        str,
        str,
    ],
    VoiceTTSResult,
]


class VoiceCallbackTTSProvider(
    VoiceTTSProvider
):

    def __init__(
        self,
        name: str,
        callback: TTSCallback,
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
                "TTS provider name "
                "cannot be empty"
            )

        if not callable(
            callback
        ):
            raise TypeError(
                "TTS callback must "
                "be callable"
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

    def synthesize(
        self,
        text: str,
        language: str = "pt-BR",
    ) -> VoiceTTSResult:
        if not self.available():
            raise RuntimeError(
                "TTS provider "
                f"'{self.name}' "
                "is not available"
            )

        normalized_text = str(
            text
        ).strip()

        if not normalized_text:
            raise ValueError(
                "TTS text cannot be empty"
            )

        result = self._callback(
            normalized_text,
            language,
        )

        if not isinstance(
            result,
            VoiceTTSResult,
        ):
            raise TypeError(
                "TTS callback must return "
                "VoiceTTSResult"
            )

        if not result.provider:
            result.provider = self.name

        result.metadata.setdefault(
            "provider",
            self.name,
        )

        result.metadata.setdefault(
            "language",
            language,
        )

        return result
