class DeviceAdapter:
    def __init__(self, device):
        if device is None:
            raise ValueError(
                "Dispositivo não informado."
            )

        self.device = device

    def execute(
        self,
        action,
        parameters=None,
        context=None,
    ):
        if not getattr(
            self.device,
            "enabled",
            True,
        ):
            return False

        parameters = dict(
            parameters or {}
        )

        action = str(action)

        method = getattr(
            self.device,
            action,
            None,
        )

        if callable(method):
            try:
                return method(
                    **parameters
                )

            except TypeError:
                if context is not None:
                    try:
                        return method(
                            context=context,
                            **parameters,
                        )
                    except TypeError:
                        pass

                return method()

        execute = getattr(
            self.device,
            "execute",
            None,
        )

        if callable(execute):
            try:
                return execute(
                    action,
                    parameters,
                )
            except TypeError:
                return execute(action)

        return False

    def read(
        self,
        attribute,
        default=None,
    ):
        attribute = str(attribute)

        state = getattr(
            self.device,
            "state",
            None,
        )

        if (
            isinstance(state, dict)
            and attribute in state
        ):
            return state[
                attribute
            ]

        return getattr(
            self.device,
            attribute,
            default,
        )

    def write(
        self,
        attribute,
        value,
    ):
        setter = getattr(
            self.device,
            "set_state",
            None,
        )

        if callable(setter):
            return setter(
                attribute,
                value,
            )

        setattr(
            self.device,
            str(attribute),
            value,
        )

        return value

    def initialize(self):
        method = getattr(
            self.device,
            "initialize",
            None,
        )

        if callable(method):
            return method()

        return False

    def shutdown(self):
        method = getattr(
            self.device,
            "shutdown",
            None,
        )

        if callable(method):
            return method()

        return False
