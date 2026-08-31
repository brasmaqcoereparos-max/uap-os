"""
Motor central de execução do Runtime UAP.

Responsabilidades:
- inicializar o runtime;
- executar instruções;
- controlar LABEL/GOTO;
- controlar CALL/RETURN;
- manter estado de execução;
- encaminhar instruções ao RuntimeInstructionSet.

Compatível com instruções no formato:

{
    "instruction": "SET",
    "arguments": ["motor", True]
}

Também aceita:

{
    "opcode": "SET",
    "operands": ["motor", True]
}
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)

from app.modules.simulator.programming.simulator.runtime.runtime_initializer import (
    RuntimeInitializer,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_goto import (
    RuntimeGoto,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_call import (
    RuntimeCall,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_return import (
    RuntimeReturn,
)


class RuntimeEngine:

    def __init__(self):

        self.initialized = False
        self.running = False

        self.last_error = None
        self.last_result = None

        self.executed_instructions = 0

        self.labels = {}
        self.routines = {}

        self.call_stack = []

        self.max_steps = 100000

    # =====================================================
    # INITIALIZATION
    # =====================================================

    def initialize(self):

        if self.initialized:
            return True

        RuntimeInitializer.initialize()

        runtime_context.reset()

        self.initialized = True
        self.last_error = None

        return True

    # =====================================================
    # LIFECYCLE
    # =====================================================

    def start(self):

        self.initialize()

        runtime_context.state.start()

        self.running = True

        return True

    def stop(self):

        runtime_context.state.stop()

        self.running = False

        return True

    def pause(self):

        runtime_context.state.pause()

        return True

    def resume(self):

        runtime_context.state.resume()

        return True

    # =====================================================
    # PROGRAM HELPERS
    # =====================================================

    @staticmethod
    def _instruction_name(
        instruction,
    ):

        if not isinstance(
            instruction,
            dict,
        ):
            return None

        name = instruction.get(
            "instruction"
        )

        if name is None:
            name = instruction.get(
                "opcode"
            )

        if name is None:
            return None

        return str(
            name
        ).upper()

    @staticmethod
    def _instruction_arguments(
        instruction,
    ):

        if not isinstance(
            instruction,
            dict,
        ):
            return []

        arguments = instruction.get(
            "arguments"
        )

        if arguments is None:
            arguments = instruction.get(
                "operands",
                [],
            )

        if arguments is None:
            return []

        if isinstance(
            arguments,
            tuple,
        ):
            return list(
                arguments
            )

        if isinstance(
            arguments,
            list,
        ):
            return arguments

        return [
            arguments
        ]

    # =====================================================
    # LABELS
    # =====================================================

    def _build_labels(
        self,
        instructions,
    ):

        self.labels = {}

        for index, instruction in enumerate(
            instructions
        ):

            if not isinstance(
                instruction,
                dict,
            ):
                continue

            if (
                self._instruction_name(
                    instruction
                )
                != "LABEL"
            ):
                continue

            arguments = (
                self._instruction_arguments(
                    instruction
                )
            )

            if not arguments:
                continue

            label = str(
                arguments[0]
            )

            self.labels[
                label
            ] = index

        return dict(
            self.labels
        )

    def get_label(
        self,
        name,
    ):

        return self.labels.get(
            str(name)
        )

    # =====================================================
    # ROUTINES
    # =====================================================

    def register_routine(
        self,
        name,
        instructions,
    ):

        if not name:
            raise ValueError(
                "Nome da rotina obrigatório."
            )

        self.routines[
            str(name)
        ] = list(
            instructions or []
        )

        return True

    def unregister_routine(
        self,
        name,
    ):

        return (
            self.routines.pop(
                str(name),
                None,
            )
            is not None
        )

    def get_routine(
        self,
        name,
    ):

        return self.routines.get(
            str(name)
        )

    def clear_routines(self):

        count = len(
            self.routines
        )

        self.routines.clear()

        return count

    # =====================================================
    # EXECUTION
    # =====================================================

    def execute(
        self,
        instructions,
    ):

        self.initialize()

        if instructions is None:
            return False

        instructions = list(
            instructions
        )

        self.last_error = None
        self.last_result = None

        self.executed_instructions = 0
        self.call_stack = []

        self._build_labels(
            instructions
        )

        try:

            self.start()

            self.last_result = (
                self._execute_program(
                    instructions
                )
            )

            return True

        except Exception as exc:

            self.last_error = str(
                exc
            )

            runtime_context.state.set_error(
                exc
            )

            return False

        finally:

            self.stop()

    def _execute_program(
        self,
        instructions,
    ):

        program_counter = 0

        steps = 0

        while (
            program_counter
            < len(instructions)
        ):

            if steps >= self.max_steps:

                raise RuntimeError(
                    "Limite máximo de passos "
                    "do runtime excedido."
                )

            if (
                runtime_context.state.paused
            ):

                break

            instruction = (
                instructions[
                    program_counter
                ]
            )

            try:

                result = (
                    self._execute_instruction(
                        instruction
                    )
                )

                self.last_result = result

                self.executed_instructions += 1

                program_counter += 1

            except RuntimeGoto as jump:

                destination = (
                    self.get_label(
                        jump.label
                    )
                )

                if destination is None:

                    raise RuntimeError(
                        f"LABEL não encontrado: "
                        f"{jump.label}"
                    )

                program_counter = (
                    destination
                )

            except RuntimeCall as call:

                result = (
                    self._execute_call(
                        call
                    )
                )

                self.last_result = result

                program_counter += 1

            except RuntimeReturn as returned:

                return (
                    returned.value
                )

            steps += 1

        return self.last_result

    # =====================================================
    # CALL
    # =====================================================

    def _execute_call(
        self,
        call,
    ):

        routine = (
            self.get_routine(
                call.routine
            )
        )

        if routine is None:

            raise RuntimeError(
                f"Rotina não encontrada: "
                f"{call.routine}"
            )

        frame = {
            "routine": call.routine,
            "arguments": list(
                call.arguments
            ),
        }

        self.call_stack.append(
            frame
        )

        try:

            result = (
                self._execute_program(
                    list(routine)
                )
            )

            return result

        finally:

            self.call_stack.pop()

    # =====================================================
    # SINGLE INSTRUCTION
    # =====================================================

    def _execute_instruction(
        self,
        instruction,
    ):

        if callable(
            instruction
        ):

            return instruction()

        if not isinstance(
            instruction,
            dict,
        ):

            return None

        name = self._instruction_name(
            instruction
        )

        arguments = (
            self._instruction_arguments(
                instruction
            )
        )

        if not name:
            return None

        handler = (
            runtime_context.instructions.get(
                name
            )
            if hasattr(
                runtime_context,
                "instructions",
            )
            else None
        )

        if not callable(
            handler
        ):

            raise RuntimeError(
                f"Instrução não registrada: "
                f"{name}"
            )

        return handler(
            *arguments
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self):

        if not self.running:
            return False

        if runtime_context.state.paused:
            return False

        runtime_context.timer.update()

        return True

    # =====================================================
    # RESET
    # =====================================================

    def reset(self):

        self.stop()

        runtime_context.reset()

        self.labels.clear()
        self.call_stack.clear()

        self.last_error = None
        self.last_result = None

        self.executed_instructions = 0

        self.initialized = False

        return True

    # =====================================================
    # STATUS
    # =====================================================

    def status(self):

        return {
            "initialized": (
                self.initialized
            ),
            "running": (
                self.running
            ),
            "paused": (
                runtime_context.state.paused
            ),
            "error": (
                self.last_error
            ),
            "last_result": (
                self.last_result
            ),
            "executed_instructions": (
                self.executed_instructions
            ),
            "label_count": len(
                self.labels
            ),
            "routine_count": len(
                self.routines
            ),
            "call_depth": len(
                self.call_stack
            ),
        }


runtime_engine = RuntimeEngine()
