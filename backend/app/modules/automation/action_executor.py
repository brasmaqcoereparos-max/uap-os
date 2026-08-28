class ActionExecutor:
    def __init__(self):
        self.handlers = {}

    def register_handler(
        self,
        action_type,
        handler,
        replace=True,
    ):
        action_type = str(
            action_type
        )

        if (
            action_type
            in self.handlers
            and not replace
        ):
            raise ValueError(
                f"Handler já registrado: "
                f"{action_type}"
            )

        if not callable(handler):
            raise TypeError(
                "Handler precisa "
                "ser executável."
            )

        self.handlers[
            action_type
        ] = handler

        return handler

    def unregister_handler(
        self,
        action_type,
    ):
        return self.handlers.pop(
            str(action_type),
            None,
        )

    def execute(
        self,
        action,
        device=None,
        context=None,
    ):
        if action is None:
            return False

        if not getattr(
            action,
            "enabled",
            True,
        ):
            return False

        action_type = str(
            getattr(
                action,
                "action_type",
                "",
            )
        )

        parameters = dict(
            getattr(
                action,
                "parameters",
                {},
            )
        )

        handler = self.handlers.get(
            action_type
        )

        if handler is not None:
            return self._call(
                handler,
                parameters,
                context=context,
            )

        if device is None:
            return False

        method = getattr(
            device,
            action_type,
            None,
        )

        if not callable(method):
            return False

        return self._call(
            method,
            parameters,
            context=context,
        )

    @staticmethod
    def _call(
        method,
        parameters,
        context=None,
    ):
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

    def has_handler(
        self,
        action_type,
    ):
        return (
            str(action_type)
            in self.handlers
        )

    def clear_handlers(self):
        self.handlers.clear()


action_executor = ActionExecutor()
