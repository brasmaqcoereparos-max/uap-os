class Device:
    def __init__(
        self,
        device_id,
        name,
        device_type="generic",
        metadata=None,
    ):
        self.id = str(device_id)
        self.device_id = self.id

        self.name = str(name)
        self.device_type = str(
            device_type
        )

        self.enabled = True
        self.initialized = False

        self.metadata = dict(
            metadata or {}
        )

        self.state = {}

    def initialize(self):
        self.initialized = True
        return True

    def update(self):
        if not self.enabled:
            return False

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

    def set_state(
        self,
        name,
        value,
    ):
        self.state[
            str(name)
        ] = value

        return value

    def get_state(
        self,
        name,
        default=None,
    ):
        return self.state.get(
            str(name),
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
