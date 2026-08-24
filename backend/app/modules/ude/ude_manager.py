from app.modules.ude.device_manager import (
    device_manager,
)

from app.modules.ude.device_factory import (
    device_factory,
)

from app.modules.ude.discovery import (
    device_discovery,
)


class UDEManager:

    def create(
        self,
        device_type,
        name,
    ):

        device = device_factory.create(
            device_type,
            name,
        )

        return self.register(
            device
        )

    def register(
        self,
        device,
    ):

        if device is None:
            raise ValueError(
                "Dispositivo não informado."
            )

        device_manager.add(
            device
        )

        device_discovery.add(
            device_id=device.id,
            name=device.name,
            device_type=device.device_type,
            protocol=getattr(
                device,
                "protocol",
                None,
            ),
            address=getattr(
                device,
                "address",
                None,
            ),
            metadata=getattr(
                device,
                "metadata",
                {},
            ),
        )

        return device

    def get(
        self,
        device_id,
    ):

        return device_manager.get(
            device_id
        )

    def all(self):

        return device_manager.list()


ude_manager = UDEManager()
