from app.modules.simulator.programming.simulator.device.device_registry import (
    device_registry,
)


class DeviceManager:

    def add(
        self,
        device,
    ):
        device_registry.register(
            device.name,
            device,
        )

        return device

    def get(
        self,
        name,
    ):
        return device_registry.get(
            name
        )

    def remove(
        self,
        name,
    ):
        return device_registry.unregister(
            name
        )

    def all(self):
        return device_registry.all()

    def update_all(self):

        for device in (
            device_registry.all().values()
        ):
            if hasattr(
                device,
                "update",
            ):
                device.update()

    def reset_all(self):

        for device in (
            device_registry.all().values()
        ):
            if hasattr(
                device,
                "reset",
            ):
                device.reset()


device_manager = DeviceManager()
