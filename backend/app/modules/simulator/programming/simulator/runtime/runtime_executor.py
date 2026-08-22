"""
Executor central de automações do UAP.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_engine import (
    runtime_engine,
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

        self.current_task = task
        self.last_result = None
        self.last_error = None

        if not callable(task):

            self.last_error = (
                "A tarefa fornecida não é executável."
            )

            self.current_task = None

            return None

        try:

            runtime_engine.start()

            self.last_result = task(
                *args,
                **kwargs,
            )

            return self.last_result

        except Exception as exc:

            self.last_error = str(exc)

            return None

        finally:

            runtime_engine.stop()
            self.current_task = None

    def update(self):

        runtime_engine.update()

    def stop(self):

        runtime_engine.stop()

    def pause(self):

        runtime_engine.pause()

    def resume(self):

        runtime_engine.resume()

    def reset(self):

        self.current_task = None
        self.last_result = None
        self.last_error = None

        runtime_engine.reset()

    def has_error(self):

        return self.last_error is not None

    def get_error(self):

        return self.last_error


runtime_executor = RuntimeExecutor()
