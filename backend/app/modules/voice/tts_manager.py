from app.modules.voice.text_tts_provider import (
    voice_text_tts_provider,
)
from app.modules.voice.tts_registry import (
    voice_tts_registry,
)


class VoiceTTSManager:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            voice_tts_registry.register(
                voice_text_tts_provider,
                default=True,
            )

            self._initialized = True

        return self

    def synthesize(
        self,
        text: str,
        language: str = "pt-BR",
        provider_name: (
            str | None
        ) = None,
    ):
        self.initialize()

        if provider_name:
            provider = (
                voice_tts_registry.get(
                    provider_name
                )
            )
        else:
            provider = (
                voice_tts_registry
                .default()
            )

        if not provider:
            raise ValueError(
                "TTS provider not found"
            )

        if not provider.available():
            raise RuntimeError(
                "TTS provider unavailable"
            )

        return provider.synthesize(
            text=text,
            language=language,
        )

    def providers(self):
        self.initialize()

        return [
            {
                "name": provider.name,
                "available": (
                    provider.available()
                ),
            }
            for provider
            in voice_tts_registry
            .list_all()
        ]


voice_tts_manager = (
    VoiceTTSManager()
          )
