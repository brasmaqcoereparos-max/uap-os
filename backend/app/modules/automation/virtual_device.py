from uuid import uuid4


class VirtualDevice:

    def __init__(
        self,
        name,
        device_type,
    ):

        self.id = str(uuid4())

        self.name = name

        self.device_type = device_type

        self.state = {}

    def set(
        self,
        name,
        value,
    ):

        self.state[name] = value

    def get(
        self,
        name,
        default=None,
    ):

        return self.state.get(
            name,
            default,
        )
