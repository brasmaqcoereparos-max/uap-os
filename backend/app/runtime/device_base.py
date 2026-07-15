from abc import ABC, abstractmethod


class DeviceBase(ABC):

    def __init__(self, device_id: str, name: str):
        self.id = device_id
        self.name = name
        self.online = False

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def update(self):
        pass

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "online": self.online,
        }
