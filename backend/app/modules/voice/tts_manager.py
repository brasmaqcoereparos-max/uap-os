from __future__ import annotations

from app.modules.voice.text_tts_provider import (
    voice_text_tts_provider,
)
from app.modules.voice.tts_provider import (
    VoiceTTSProvider,
)
from app.modules.voice.tts_registry import (
    voice_tts_registry,
)
from app.modules.voice.tts_result import (
    VoiceTTSResult,
)


class VoiceTTSManager:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            existing = (
                voice_tts_registry.get(
                    voice_text_tts_provider.name
                )
            )

            if existing is None:
                voice_tts_registry.register(
                    voice_text_tts_provider,
                    default=True,
                )

            elif (
                voice_tts_registry.default()
                is None
            ):
                voice_tts_registry.set_default(
                    voice_text_tts_provider.name
                )

            self._initialized = True

        return self

    def register(
        self,
        provider: VoiceTTSProvider,
        *,
        default: bool = False,
    ):
        self.initialize()

        if not isinstance(
            provider,
            VoiceTTSProvider,
        ):
            raise TypeError(
                "provider must implement "
                "VoiceTTSProvider"
            )

        return (
            voice_tts_registry.register(
                provider,
                default=default,
            )
        )

    def set_default(
        self,
        provider_name: str,
    ):
        self.initialize()

        return (
            voice_tts_registry.set_default(
                provider_name
            )
        )

    def get(
        self,
        provider_name: str,
    ):
        self.initialize()

        return (
            voice_tts_registry.get(
                provider_name
            )
        )

    def synthesize(
        self,
        text: str,
        language: str = "pt-BR",
        provider_name: (
            str | None
        ) = None,
    ) -> VoiceTTSResult:
        self.initialize()

        normalized_text = str(
            text
        ).strip()

        if not normalized_text:
            raise ValueError(
                "TTS text cannot be empty"
            )

        normalized_language = str(
            language
        ).strip()

        if not normalized_language:
            normalized_language = (
                "pt-BR"
            )

        if provider_name:
            provider = (
                voice_tts_registry.get(
                    provider_name
                )
            )
        else:
            provider = (
                voice_tts_registry.default()
            )

        if not provider:
            raise ValueError(
                "TTS provider not found"
            )

        if not provider.available():
            raise RuntimeError(
                "TTS provider "
                f"'{provider.name}' "
                "is unavailable"
            )

        result = provider.synthesize(
            text=normalized_text,
            language=normalized_language,
        )

        if not isinstance(
            result,
            VoiceTTSResult,
        ):
            raise TypeError(
                "TTS provider must return "
                "VoiceTTSResult"
            )

        result.metadata.setdefault(
            "language",
            normalized_language,
        )

        result.metadata.setdefault(
            "provider",
            provider.name,
        )

        return result

    def providers(self):
        self.initialize()

        default_provider = (
            voice_tts_registry.default()
        )

        return [
            {
                "name": provider.name,
                "available": (
                    provider.available()
                ),
                "default": (
                    default_provider
                    is provider
                ),
            }
            for provider
            in voice_tts_registry
            .list_all()
        ]


voice_tts_manager = (
    VoiceTTSManager()
)
