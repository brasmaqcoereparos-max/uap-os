
from app.modules.simulator.programming.simulator.peripheral_sdk.peripheral_registry import (
    peripheral_registry,
)


class PeripheralFactory:

    def create(

        self,

        name,

        *args,

        **kwargs,

    ):

        peripheral = peripheral_registry.get(

            name,

        )

        if peripheral is None:

            raise ValueError(

                f"Periférico '{name}' não encontrado."

            )

        return peripheral(

            *args,

            **kwargs,

        )


peripheral_factory = PeripheralFactory()
