from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_registry import (
    peripheral_registry,
)

from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_validator import (
    peripheral_validator,
)


class PeripheralGenerator:

    def register(

        self,

        peripheral_class,

    ):

        peripheral_validator.validate(

            peripheral_class,

        )

        peripheral_registry.register(

            peripheral_class,

        )


peripheral_generator = PeripheralGenerator()
