from app.runtime.runtime_gateway import (
    runtime_gateway,
)

from app.runtime.runtime_events import (
    runtime_events,
)


class RuntimeExecutor:

    def execute(
        self,
        command,
    ):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando inválido."
            )

        try:

            result = runtime_gateway.execute(
                command
            )

            runtime_events.emit(
                "runtime.command.completed",
                "runtime_executor",
                {
                    "command": command,
                    "result": result,
                },
            )

            return result

        except Exception as exc:

            runtime_events.emit(
                "runtime.command.error",
                "runtime_executor",
                {
                    "command": command,
                    "error": str(exc),
                },
            )

            raise

    def execute_many(
        self,
        commands,
    ):

        results = []

        for command in commands:

            results.append(
                self.execute(command)
            )

        return results


runtime_executor = RuntimeExecutor()
