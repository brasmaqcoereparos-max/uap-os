class DeviceBinding:
    def __init__(
        self,
        block_id,
        device_id=None,
        metadata=None,
    ):
        self.block_id = str(
            block_id
        )

        self.device_id = (
            str(device_id)
            if device_id is not None
            else None
        )

        self.metadata = dict(
            metadata or {}
        )

    def bind(self, device_id):
        if device_id is None:
            raise ValueError(
                "device_id não informado."
            )

        self.device_id = str(
            device_id
        )

        return self.device_id

    def unbind(self):
        previous = self.device_id
        self.device_id = None

        return previous

    def is_bound(self):
        return self.device_id is not None

    def matches_block(
        self,
        block_id,
    ):
        return (
            self.block_id
            == str(block_id)
        )

    def matches_device(
        self,
        device_id,
    ):
        return (
            self.device_id
            == str(device_id)
        )

    def to_dict(self):
        return {
            "block_id": self.block_id,
            "device_id": self.device_id,
            "bound": self.is_bound(),
            "metadata": dict(
                self.metadata
            ),
        }
