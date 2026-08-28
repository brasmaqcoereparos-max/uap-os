from uuid import uuid4


class VirtualDevice:
    def __init__(
        self,
        name,
        device_type,
        device_id=None,
        metadata=None,
    ):
        self.id = (
            str(device_id)
            if device_id is not None
            else str(uuid4())
        )

        self.device_id = self.id

        self.name = str(name)
        self.device_type = str(
            device_type
        )

        self.state = {}

        self.enabled = True
        self.initialized = False

        self.metadata = dict(
            metadata or {}
        )

    def initialize(self):
        self.initialized = True
        return True

    def shutdown(self):
        self.initialized = False
        return True

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def set(
        self,
        name,
        value,
    ):
        self.state[
            str(name)
        ] = value

        return value

    def set_state(
        self,
        name,
        value,
    ):
        return self.set(
            name,
            value,
        )

    def get(
        self,
        name,
        default=None,
    ):
        return self.state.get(
            str(name),
            default,
        )

    def get_state(
        self,
        name,
        default=None,
    ):
        return self.get(
            name,
            default,
        )

    def execute(
        self,
        action,
        parameters=None,
    ):
        if not self.enabled:
            return False

        method = getattr(
            self,
            str(action),
            None,
        )

        if not callable(method):
            return False

        parameters = dict(
            parameters or {}
        )

        return method(
            **parameters
        )

    def update(self):
        return self.enabled

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.device_type,
            "enabled": self.enabled,
            "initialized": (
                self.initialized
            ),
            "state": dict(
                self.state
            ),
            "metadata": dict(
                self.metadata
            ),
    }
