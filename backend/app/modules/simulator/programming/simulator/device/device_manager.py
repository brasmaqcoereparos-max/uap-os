"""
Gerenciador central das instâncias de dispositivos UAP.
"""

from app.modules.simulator.programming.simulator.device.device_registry import (
    device_registry,
)


class DeviceManager:
    def add(
        self,
        device,
        replace=True,
    ):
        if device is None:
            raise ValueError(
                "Dispositivo não pode "
                "ser None."
            )

        name = getattr(
            device,
            "name",
            None,
        )

        if not name:
            raise ValueError(
                "Dispositivo sem nome."
            )

        return device_registry.register(
            name,
            device,
            replace=replace,
        )

    def get(self, name):
        return device_registry.get(
            name
        )

    def remove(self, name):
        return device_registry.unregister(
            name
        )

    def exists(self, name):
        return device_registry.exists(
            name
        )

    def all(self):
        return device_registry.all()

    def values(self):
        return device_registry.values()

    def names(self):
        return device_registry.names()

    def count(self):
        return device_registry.count()

    def initialize_all(self):
        results = {}

        for name, device in (
            self.all().items()
        ):
            initialize = getattr(
                device,
                "initialize",
                None,
            )

            if callable(initialize):
                try:
                    results[name] = (
                        initialize()
                    )
                except Exception as exc:
                    results[name] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def update_all(self):
        results = {}

        for name, device in (
            self.all().items()
        ):
            if not getattr(
                device,
                "enabled",
                True,
            ):
                continue

            update = getattr(
                device,
                "update",
                None,
            )

            if callable(update):
                try:
                    results[name] = (
                        update()
                    )
                except Exception as exc:
                    results[name] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def reset_all(self):
        results = {}

        for name, device in (
            self.all().items()
        ):
            reset = getattr(
                device,
                "reset",
                None,
            )

            if callable(reset):
                try:
                    results[name] = (
                        reset()
                    )
                except Exception as exc:
                    results[name] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def clear(self):
        return device_registry.clear()


device_manager = DeviceManager()
