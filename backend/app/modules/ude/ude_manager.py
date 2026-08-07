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

        device_manager.add(device)

        return device

    def register(
        self,
        device,
    ):

        device_manager.add(device)

        device_discovery.add(device)

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
