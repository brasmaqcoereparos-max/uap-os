"""
Fábrica central para criação de dispositivos UAP.
"""

from app.modules.simulator.programming.simulator.device.device_catalog import (
    device_catalog,
)


class DeviceFactory:
    def create(
        self,
        device_type,
        *args,
        **kwargs,
    ):
        device_class = (
            device_catalog.get(
                device_type
            )
        )

        if device_class is None:
            raise ValueError(
                "Dispositivo não "
                f"registrado: {device_type}"
            )

        return device_class(
            *args,
            **kwargs,
        )

    def create_from_definition(
        self,
        definition,
    ):
        if not isinstance(
            definition,
            dict,
        ):
            raise TypeError(
                "Definição precisa "
                "ser um dicionário."
            )

        device_type = (
            definition.get("type")
            or definition.get(
                "device_type"
            )
        )

        if not device_type:
            raise ValueError(
                "Tipo do dispositivo "
                "não informado."
            )

        arguments = dict(
            definition.get(
                "parameters",
                {},
            )
        )

        if (
            "name" in definition
            and "name"
            not in arguments
        ):
            arguments["name"] = (
                definition["name"]
            )

        return self.create(
            device_type,
            **arguments,
        )

    def exists(self, device_type):
        return device_catalog.exists(
            device_type
        )

    def available_devices(self):
        return device_catalog.all()

    def available_metadata(self):
        return device_catalog.metadata()

    def search(self, text):
        return device_catalog.search(
            text
        )

    def count(self):
        return device_catalog.count()


device_factory = DeviceFactory()
