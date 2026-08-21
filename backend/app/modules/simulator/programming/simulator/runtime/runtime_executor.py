"""
Executor de automações do UAP.

Executa funções Python previamente preparadas pelo sistema,
sem exigir que o usuário final escreva código.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_manager import (
    runtime_manager,
)


class RuntimeExecutor:

    def __init__(self):

        self.current_task = None
        self.last_result = None
        self.last_error = None

    def execute(
        self,
        task,
        *args,
        **kwargs,
    ):

        self.last_error = None
        self.last_result = None
        self.current_task = task

        if not callable(task):

            self.last_error = (
                "A tarefa fornecida não é executável."
            )

            return None

        try:

            runtime_manager.start()

            self.last_result = task(
                *args,
                **kwargs,
            )

            return self.last_result

        except Exception as exc:

            self.last_error = str(exc)

            return None

        finally:

            self.current_task = None

    def update(self):

        runtime_manager.update()

    def stop(self):

        runtime_manager.stop()

    def reset(self):

        self.current_task = None
        self.last_result = None
        self.last_error = None

        runtime_manager.reset()

    def has_error(self):

        return self.last_error is not None

    def get_error(self):

        return self.last_error


runtime_executor = RuntimeExecutor()
