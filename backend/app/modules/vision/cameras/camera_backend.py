from abc import ABC, abstractmethod
from typing import Any


class CameraBackend(ABC):

    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def capture(self):
        raise NotImplementedError

    @abstractmethod
    def status(self):
        raise NotImplementedError

    def available(self):
        status = self.status()

        return bool(
            status.get("available", False)
        )

    def __enter__(self):
        self.start()
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        self.stop()
