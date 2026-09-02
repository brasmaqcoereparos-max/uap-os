from app.modules.voice.audio_buffer import (
    VoiceAudioBuffer,
)
from app.modules.voice.recognizer import (
    VoiceRecognizer,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceTextRecognizer(
    VoiceRecognizer
):

    @property
    def name(self):
        return "text"

    def available(self):
        return True

    def recognize(
        self,
        audio: VoiceAudioBuffer,
        language: str = "pt-BR",
    ):
        try:
            text = (
                audio.data()
                .decode("utf-8")
            )

        except UnicodeDecodeError:
            text = ""

        return VoiceTranscript(
            text=text,
            language=language,
            confidence=1.0,
            final=audio.final(),
            metadata={
                "recognizer": self.name,
                "simulation": True,
            },
        )


voice_text_recognizer = (
    VoiceTextRecognizer()
)
