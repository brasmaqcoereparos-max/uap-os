from abc import ABC, abstractmethod


class DriverBase(ABC):

    def __init__(self, driver_id: str, name: str):
        self.id = driver_id
        self.name = name
        self.connected = False

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "connected": self.connected,
        }
