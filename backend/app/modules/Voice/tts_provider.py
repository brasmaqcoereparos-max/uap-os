from abc import ABC
from abc import abstractmethod

from app.modules.voice.tts_result import (
    VoiceTTSResult,
)


class VoiceTTSProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def available(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def synthesize(
        self,
        text: str,
        language: str = "pt-BR",
    ) -> VoiceTTSResult:
        raise NotImplementedError
