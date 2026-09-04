from abc import ABC
from abc import abstractmethod
from typing import Any


class CommunicationTransport(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def available(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def send(
        self,
        destination: str,
        payload: dict[str, Any],
    ):
        raise NotImplementedError
