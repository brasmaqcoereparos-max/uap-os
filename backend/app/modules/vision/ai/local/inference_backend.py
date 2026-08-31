from abc import ABC, abstractmethod
from typing import Any


class InferenceBackend(ABC):

    @abstractmethod
    def load(self):
        raise NotImplementedError

    @abstractmethod
    def infer(
        self,
        frame: Any,
    ):
        raise NotImplementedError

    @abstractmethod
    def unload(self):
        raise NotImplementedError

    @abstractmethod
    def status(self):
        raise NotImplementedError
