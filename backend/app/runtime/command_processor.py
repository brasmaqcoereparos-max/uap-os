"""
Processador central de comandos do Runtime UAP.
"""

from app.runtime.command_queue import (
    command_queue,
)

from app.runtime.logger import (
    runtime_logger,
)


class CommandProcessor:

    def __init__(self):

        self.handlers = {}

    def register(
        self,
        action,
        handler,
    ):

        if not action:
            raise ValueError(
                "Ação obrigatória."
            )

        if not callable(handler):
            raise TypeError(
                "Handler deve ser chamável."
            )

        self.handlers[
            str(action).strip().lower()
        ] = handler

    def unregister(
        self,
        action,
    ):

        return self.handlers.pop(
            str(action).strip().lower(),
            None,
        )

    def process(self):

        processed = 0

        while True:

            command = command_queue.get()

            if command is None:
                break

            processed += 1

            try:

                self.execute(
                    command
                )

            except Exception as exc:

                runtime_logger.error(
                    str(exc)
                )

        return processed

    def execute(
        self,
        command,
    ):

        if not isinstance(
            command,
            dict,
        ):

            raise TypeError(
                "Comando Runtime inválido."
            )

        action = command.get(
            "action"
        )

        if not action:

            raise ValueError(
                "Comando sem action."
            )

        action = str(
            action
        ).strip().lower()

        handler = self.handlers.get(
            action
        )

        if handler is None:

            runtime_logger.warning(
                f"Unknown command: {action}"
            )

            return None

        result = handler(
            command
        )

        runtime_logger.info(
            f"Command executed: {action}"
        )

        return result


command_processor = CommandProcessor()
