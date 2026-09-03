from abc import ABC
from abc import abstractmethod

from app.modules.ai.request import (
    AIRequest,
)
from app.modules.ai.response import (
    AIResponse,
)


class AIProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def available(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def generate(
        self,
        request: AIRequest,
    ) -> AIResponse:
        raise NotImplementedError
