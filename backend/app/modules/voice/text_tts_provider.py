from app.modules.voice.tts_provider import (
    VoiceTTSProvider,
)
from app.modules.voice.tts_result import (
    VoiceTTSResult,
)


class VoiceTextTTSProvider(
    VoiceTTSProvider
):

    @property
    def name(self):
        return "text"

    def available(self):
        return True

    def synthesize(
        self,
        text: str,
        language: str = "pt-BR",
    ):
        return VoiceTTSResult(
            provider=self.name,
            text=text,
            audio=None,
            mime_type=None,
            success=True,
            metadata={
                "simulation": True,
                "language": language,
            },
        )


voice_text_tts_provider = (
    VoiceTextTTSProvider()
)
