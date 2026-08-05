from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class DriverLoader:

    def load(

        self,

        name,

    ):

        return hardware_registry.get(name)


driver_loader = DriverLoader()
