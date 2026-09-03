from app.modules.voice.tts_provider import (
    VoiceTTSProvider,
)


class VoiceTTSRegistry:

    def __init__(self):
        self._providers: dict[
            str,
            VoiceTTSProvider,
        ] = {}

        self._default: str | None = None

    def register(
        self,
        provider: VoiceTTSProvider,
        default: bool = False,
    ):
        self._providers[
            provider.name
        ] = provider

        if (
            default
            or self._default is None
        ):
            self._default = (
                provider.name
            )

        return provider

    def get(
        self,
        name: str,
    ):
        return self._providers.get(
            name
        )

    def default(self):
        if self._default is None:
            return None

        return self.get(
            self._default
        )

    def set_default(
        self,
        name: str,
    ):
        if name not in self._providers:
            raise ValueError(
                "TTS provider not found"
            )

        self._default = name

        return self.get(name)

    def available(self):
        return [
            provider
            for provider
            in self._providers.values()
            if provider.available()
        ]

    def list_all(self):
        return list(
            self._providers.values()
        )


voice_tts_registry = (
    VoiceTTSRegistry()
)
