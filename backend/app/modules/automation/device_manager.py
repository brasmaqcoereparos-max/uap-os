from app.modules.automation.device_registry import (
    device_registry,
)


class DeviceManager:
    def initialize_all(self):
        results = {}

        for device in device_registry.all():
            device_id = str(
                getattr(
                    device,
                    "device_id",
                    getattr(
                        device,
                        "id",
                        "",
                    ),
                )
            )

            initialize = getattr(
                device,
                "initialize",
                None,
            )

            if not callable(initialize):
                results[device_id] = False
                continue

            try:
                results[
                    device_id
                ] = initialize()

            except Exception:
                results[
                    device_id
                ] = False

        return results

    def update_all(self):
        results = {}

        for device in device_registry.all():
            if not getattr(
                device,
                "enabled",
                True,
            ):
                continue

            device_id = str(
                getattr(
                    device,
                    "device_id",
                    getattr(
                        device,
                        "id",
                        "",
                    ),
                )
            )

            update = getattr(
                device,
                "update",
                None,
            )

            if not callable(update):
                continue

            try:
                results[
                    device_id
                ] = update()

            except Exception:
                results[
                    device_id
                ] = False

        return results

    def shutdown_all(self):
        results = {}

        for device in device_registry.all():
            device_id = str(
                getattr(
                    device,
                    "device_id",
                    getattr(
                        device,
                        "id",
                        "",
                    ),
                )
            )

            shutdown = getattr(
                device,
                "shutdown",
                None,
            )

            if not callable(shutdown):
                results[device_id] = False
                continue

            try:
                results[
                    device_id
                ] = shutdown()

            except Exception:
                results[
                    device_id
                ] = False

        return results

    def get(self, device_id):
        return device_registry.get(
            str(device_id)
        )

    def register(
        self,
        device,
        device_id=None,
    ):
        if device_id is None:
            device_id = getattr(
                device,
                "device_id",
                getattr(
                    device,
                    "id",
                    None,
                ),
            )

        if device_id is None:
            raise ValueError(
                "Dispositivo sem ID."
            )

        return device_registry.register(
            str(device_id),
            device,
        )

    def unregister(
        self,
        device_id,
    ):
        return device_registry.unregister(
            str(device_id)
        )


device_manager = DeviceManager()
