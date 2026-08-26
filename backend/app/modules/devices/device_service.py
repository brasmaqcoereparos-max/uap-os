from app.modules.devices.device_registry import (
    device_registry,
)


class DeviceService:

    def register(self, device):
        return device_registry.register(
            device
        )

    def unregister(self, device_id):
        return device_registry.unregister(
            device_id
        )

    def get(self, device_id):
        return device_registry.get(
            device_id
        )

    def list(self):
        return device_registry.list()

    def count(self):
        return device_registry.count()

    def connect(self, device_id):

        device = self._require(
            device_id
        )

        return device.connect()

    def disconnect(self, device_id):

        device = self._require(
            device_id
        )

        return device.disconnect()

    def read(self, device_id):

        device = self._require(
            device_id
        )

        return device.read()

    def write(
        self,
        device_id,
        value,
    ):

        device = self._require(
            device_id
        )

        return device.write(value)

    def update(self, device_id):

        device = self._require(
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

        device = self._require(
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

    def _require(self, device_id):

        device = device_registry.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        return device


device_service = DeviceService()
