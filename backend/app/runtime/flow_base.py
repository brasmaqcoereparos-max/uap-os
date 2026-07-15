from abc import ABC, abstractmethod


class FlowBase(ABC):

    def __init__(self, flow_id: str, name: str):
        self.id = flow_id
        self.name = name
        self.enabled = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "enabled": self.enabled,
        }
