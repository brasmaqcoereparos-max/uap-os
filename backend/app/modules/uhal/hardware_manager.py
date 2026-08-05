from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class HardwareManager:

    def __init__(self):

        self.current_driver = None

    def load(

        self,

        name,

    ):

        self.current_driver = hardware_registry.get(name)

        return self.current_driver

    def current(self):

        return self.current_driver


hardware_manager = HardwareManager()
