from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class HALManager:

    def __init__(self):

        self.driver = None

    def load(

        self,

        board,

    ):

        self.driver = hardware_registry.get(

            board,

        )

        return self.driver

    def current(self):

        return self.driver

    def available(self):

        return hardware_registry.all()


hal_manager = HALManager()
