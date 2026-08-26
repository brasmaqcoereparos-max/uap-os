from app.modules.devices.device_registry import (
    device_registry,
)


class RuntimeDeviceBridge:

    def resolve(
        self,
        device_id,
    ):

        device = device_registry.get(
            device_id
        )

        if device is None:
            raise KeyError(
                f"Dispositivo '{device_id}' não encontrado."
            )

        return device

    def connect(
        self,
        device_id,
    ):

        device = self.resolve(
            device_id
        )

        return device.connect()

    def disconnect(
        self,
        device_id,
    ):

        device = self.resolve(
            device_id
        )

        return device.disconnect()

    def read(
        self,
        device_id,
    ):

        device = self.resolve(
            device_id
        )

        return device.read()

    def write(
        self,
        device_id,
        value,
    ):

        device = self.resolve(
            device_id
        )

        return device.write(
            value
        )

    def status(
        self,
        device_id,
    ):

        device = self.resolve(
            device_id
        )

        status = getattr(
            device,
            "status",
            None,
        )

        if callable(status):
            return status()

        return {
            "id": device_id,
        }


runtime_device_bridge = (
    RuntimeDeviceBridge()
      )
