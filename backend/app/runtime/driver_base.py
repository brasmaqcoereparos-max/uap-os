from abc import ABC, abstractmethod


class DriverBase(ABC):

    def __init__(
        self,
        driver_id: str,
        name: str,
    ):
        self.id = driver_id
        self.name = name
        self.connected = False

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    def initialize(self):
        return self.connect()

    def shutdown(self):
        return self.disconnect()

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "connected": self.connected,
        }
