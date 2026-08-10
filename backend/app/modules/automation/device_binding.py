class DeviceBinding:

    def __init__(
        self,
        block_id,
        device_id=None,
    ):

        self.block_id = block_id
        self.device_id = device_id

    def bind(
        self,
        device_id,
    ):

        self.device_id = device_id

    def unbind(self):

        self.device_id = None

    def is_bound(self):

        return self.device_id is not None
