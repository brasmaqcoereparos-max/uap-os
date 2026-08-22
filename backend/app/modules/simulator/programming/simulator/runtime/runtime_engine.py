"""
Motor de execução do runtime UAP.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)

from app.modules.simulator.programming.simulator.runtime.runtime_initializer import (
    RuntimeInitializer,
)


class RuntimeEngine:

    def __init__(self):

        self.initialized = False
        self.running = False
        self.last_error = None

    def initialize(self):

        if self.initialized:
            return

        RuntimeInitializer.initialize()

        runtime_context.reset()

        self.initialized = True
        self.last_error = None

    def start(self):

        self.initialize()

        runtime_context.state.start()

        self.running = True

    def stop(self):

        runtime_context.state.stop()

        self.running = False

    def pause(self):

        runtime_context.state.pause()

    def resume(self):

        runtime_context.state.resume()

    def execute(
        self,
        instructions,
    ):

        self.initialize()

        if instructions is None:
            return False

        try:

            self.start()

            for instruction in instructions:

                if callable(instruction):

                    instruction()

                elif isinstance(
                    instruction,
                    dict,
                ):

                    self._execute_instruction(
                        instruction
                    )

            return True

        except Exception as exc:

            self.last_error = str(exc)
            runtime_context.state.set_error(
                exc
            )

            return False

        finally:

            self.stop()

    def _execute_instruction(
        self,
        instruction,
    ):

        name = instruction.get(
            "instruction"
        )

        arguments = instruction.get(
            "arguments",
            [],
        )

        if not name:
            return

        handler = (
            runtime_context.instructions.get(
                str(name).upper()
            )
            if hasattr(
                runtime_context,
                "instructions",
            )
            else None
        )

        if callable(handler):

            handler(*arguments)

    def update(self):

        if not self.running:
            return

        if runtime_context.state.paused:
            return

        runtime_context.timer.update()

    def reset(self):

        self.stop()
        runtime_context.reset()
        self.last_error = None
        self.initialized = False


runtime_engine = RuntimeEngine()
