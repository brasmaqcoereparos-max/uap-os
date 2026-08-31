"""
Executor universal de ações da automação UAP.

Mantém o contrato existente:
    register_handler()
    unregister_handler()
    execute()
    has_handler()
    clear_handlers()
    action_executor

A execução segue:

Action
  ↓
Handler registrado
  OU
Método do dispositivo
"""

class ActionExecutor:

    def __init__(self):
        self.handlers = {}

        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.last_action = None
        self.last_result = None
        self.last_error = None

    def register_handler(
        self,
        action_type,
        handler,
        replace=True,
    ):
        action_type = str(
            action_type
        )

        if not action_type:
            raise ValueError(
                "action_type não pode "
                "ser vazio."
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

        if not callable(
            handler
        ):
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

    def get_handler(
        self,
        action_type,
    ):
        return self.handlers.get(
            str(action_type)
        )

    def execute(
        self,
        action,
        device=None,
        context=None,
    ):
        self.last_action = action
        self.last_result = None
        self.last_error = None

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

        handler = (
            self.handlers.get(
                action_type
            )
        )

        try:
            if handler is not None:
                result = self._call(
                    handler,
                    parameters,
                    context=context,
                )

            else:
                if device is None:
                    result = False

                else:
                    method = getattr(
                        device,
                        action_type,
                        None,
                    )

                    if not callable(method):
                        result = False

                    else:
                        result = self._call(
                            method,
                            parameters,
                            context=context,
                        )

            success = (
                result is not False
            )

            self.execution_count += 1

            if success:
                self.success_count += 1
            else:
                self.failure_count += 1

            self.last_result = result

            marker = getattr(
                action,
                "mark_result",
                None,
            )

            if callable(marker):
                marker(
                    result=result,
                    success=success,
                )

            return result

        except Exception as exc:
            self.execution_count += 1
            self.failure_count += 1

            self.last_error = str(exc)

            marker = getattr(
                action,
                "mark_result",
                None,
            )

            if callable(marker):
                marker(
                    result=None,
                    success=False,
                    error=exc,
                )

            raise

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

        except TypeError as first_error:
            if context is not None:
                try:
                    return method(
                        context=context,
                        **parameters,
                    )

                except TypeError:
                    pass

            try:
                return method()

            except TypeError:
                raise first_error

    def has_handler(
        self,
        action_type,
    ):
        return (
            str(action_type)
            in self.handlers
        )

    def list_handlers(self):
        return list(
            self.handlers.keys()
        )

    def handler_count(self):
        return len(
            self.handlers
        )

    def clear_handlers(self):
        count = len(
            self.handlers
        )

        self.handlers.clear()

        return count

    def reset_statistics(self):
        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.last_action = None
        self.last_result = None
        self.last_error = None

        return True

    def status(self):
        return {
            "handler_count": (
                self.handler_count()
            ),
            "handlers": (
                self.list_handlers()
            ),
            "execution_count": (
                self.execution_count
            ),
            "success_count": (
                self.success_count
            ),
            "failure_count": (
                self.failure_count
            ),
            "last_error": (
                self.last_error
            ),
        }


action_executor = (
    ActionExecutor()
    )
