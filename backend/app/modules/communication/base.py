from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class CommunicationError(Exception):
    pass


class CommunicationChannel(ABC):

    protocol: str = "unknown"

    @abstractmethod
    async def connect(self, **kwargs: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def send(self, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def receive(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def is_connected(self) -> bool:
        raise NotImplementedError
