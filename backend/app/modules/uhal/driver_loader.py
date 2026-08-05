from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class DriverLoader:

    def load(

        self,

        name,

    ):

        return hardware_registry.get(name)

    def available(self):

        return hardware_registry.all()


driver_loader = DriverLoader()
