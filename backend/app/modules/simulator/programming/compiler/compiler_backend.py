from abc import ABC, abstractmethod


class CompilerBackend(ABC):

    name = "generic"

    @abstractmethod
    def generate(
        self,
        ir,
    ):

        pass
