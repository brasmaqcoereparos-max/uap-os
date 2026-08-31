from abc import ABC, abstractmethod
from typing import Any


class AIModel(ABC):

    @abstractmethod
    def load(self):
        raise NotImplementedError

    @abstractmethod
    def predict(self, frame: Any):
        raise NotImplementedError

    @abstractmethod
    def status(self):
        raise NotImplementedError

    def is_loaded(self):
        return bool(
            self.status().get(
                "loaded",
                False,
            )
        )
