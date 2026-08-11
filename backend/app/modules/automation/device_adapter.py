class DeviceAdapter:

    def __init__(
        self,
        device,
    ):

        self.device = device

    def execute(
        self,
        action,
        parameters=None,
    ):

        parameters = parameters or {}

        method = getattr(
            self.device,
            action,
            None,
        )

        if method is None:
            return False

        method(
            **parameters
        )

        return True

    def read(
        self,
        attribute,
        default=None,
    ):

        return getattr(
            self.device,
            attribute,
            default,
        )
