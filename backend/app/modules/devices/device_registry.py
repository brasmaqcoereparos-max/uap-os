class DeviceRegistry:

    def __init__(self):
        self._devices = {}

    def register(
        self,
        device,
    ):
        device_id = getattr(
            device,
            "id",
            None,
        )

        if not device_id:
            raise ValueError(
                "Dispositivo sem id."
            )

        self._devices[
            str(device_id)
        ] = device

        return device

    def unregister(
        self,
        device_id,
    ):
        return self._devices.pop(
            str(device_id),
            None,
        )

    def get(
        self,
        device_id,
    ):
        return self._devices.get(
            str(device_id)
        )

    def exists(
        self,
        device_id,
    ):
        return str(
            device_id
        ) in self._devices

    def all(self):
        return dict(
            self._devices
        )

    def clear(self):
        self._devices.clear()

    def count(self):
        return len(
            self._devices
        )


device_registry = DeviceRegistry()
