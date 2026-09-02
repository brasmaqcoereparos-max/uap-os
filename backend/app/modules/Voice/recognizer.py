from abc import ABC
from abc import abstractmethod

from app.modules.voice.audio_buffer import (
    VoiceAudioBuffer,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


class VoiceRecognizer(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def available(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def recognize(
        self,
        audio: VoiceAudioBuffer,
        language: str = "pt-BR",
    ) -> VoiceTranscript:
        raise NotImplementedError
