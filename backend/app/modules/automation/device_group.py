class DeviceGroup:
    def __init__(
        self,
        name,
        metadata=None,
    ):
        self.name = str(name)
        self.devices = []

        self.metadata = dict(
            metadata or {}
        )

    def add(self, device):
        if device is None:
            return False

        if device not in self.devices:
            self.devices.append(
                device
            )

        return device

    def remove(self, device):
        if device not in self.devices:
            return False

        self.devices.remove(
            device
        )

        return True

    def get(
        self,
        device_id,
    ):
        device_id = str(
            device_id
        )

        for device in self.devices:
            current_id = str(
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

            if current_id == device_id:
                return device

        return None

    def contains(
        self,
        device_id,
    ):
        return (
            self.get(device_id)
            is not None
        )

    def all(self):
        return list(
            self.devices
        )

    def enabled(self):
        return [
            device
            for device in self.devices
            if getattr(
                device,
                "enabled",
                True,
            )
        ]

    def clear(self):
        self.devices.clear()

    def count(self):
        return len(
            self.devices
        )

    def to_dict(self):
        return {
            "name": self.name,
            "count": self.count(),
            "devices": [
                (
                    device.to_dict()
                    if hasattr(
                        device,
                        "to_dict",
                    )
                    else str(device)
                )
                for device in self.devices
            ],
            "metadata": dict(
                self.metadata
            ),
    }
