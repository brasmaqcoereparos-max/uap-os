from app.modules.devices.device_registry import (
    device_registry,
)


class RuntimeDeviceBridge:

    def resolve(self, device_id):
        device = device_registry.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        return device

    def connect(self, device_id):
        return self.resolve(
            device_id
        ).connect()

    def disconnect(self, device_id):
        return self.resolve(
            device_id
        ).disconnect()

    def read(self, device_id):
        return self.resolve(
            device_id
        ).read()

    def write(
        self,
        device_id,
        value,
    ):
        return self.resolve(
            device_id
        ).write(value)

    def update(self, device_id):
        device = self.resolve(
            device_id
        )

        method = getattr(
            device,
            "update",
            None,
        )

        if callable(method):
            return method()

        return True

    def status(self, device_id):
        device = self.resolve(
            device_id
        )

        method = getattr(
            device,
            "status",
            None,
        )

        if callable(method):
            return method()

        return {
            "id": device_id,
        }


runtime_device_bridge = (
    RuntimeDeviceBridge()
)
