from app.modules.devices.device_factory import (
    device_factory,
)

from app.modules.devices.device_registry import (
    device_registry,
)


class DeviceLoader:

    def load(
        self,
        definition,
    ):

        if not isinstance(
            definition,
            dict,
        ):
            raise TypeError(
                "Definição de dispositivo inválida."
            )

        device = device_factory.create(
            device_type=definition.get(
                "type",
                "gpio",
            ),
            device_id=definition.get(
                "id"
            ),
            **{
                key: value
                for key, value
                in definition.items()
                if key not in {
                    "type",
                    "id",
                }
            },
        )

        device_registry.register(
            device
        )

        return device

    def load_many(
        self,
        definitions,
    ):

        devices = []

        for definition in definitions:

            devices.append(
                self.load(
                    definition
                )
            )

        return devices


device_loader = DeviceLoader()
