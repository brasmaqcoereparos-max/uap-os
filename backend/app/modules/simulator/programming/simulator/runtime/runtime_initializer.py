from app.modules.simulator.programming.simulator.runtime.runtime_instruction_set import (
    runtime_instruction_set,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_mov import instruction_mov
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_set import instruction_set
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_get import instruction_get
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_wait import instruction_wait
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_label import instruction_label
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_goto import instruction_goto
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_if import instruction_if
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_call import instruction_call
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_return import instruction_return
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_add import instruction_add
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_sub import instruction_sub
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_mul import instruction_mul
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_div import instruction_div
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_eq import instruction_eq
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_ne import instruction_ne
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_gt import instruction_gt
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_pin_mode import instruction_pin_mode
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_digital_write import instruction_digital_write
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_digital_read import instruction_digital_read


class RuntimeInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:
            return

        runtime_instruction_set.register("MOV", instruction_mov)
        runtime_instruction_set.register("SET", instruction_set)
        runtime_instruction_set.register("GET", instruction_get)
        runtime_instruction_set.register("WAIT", instruction_wait)

        runtime_instruction_set.register("LABEL", instruction_label)
        runtime_instruction_set.register("GOTO", instruction_goto)
        runtime_instruction_set.register("IF", instruction_if)
        runtime_instruction_set.register("CALL", instruction_call)
        runtime_instruction_set.register("RETURN", instruction_return)

        runtime_instruction_set.register("ADD", instruction_add)
        runtime_instruction_set.register("SUB", instruction_sub)
        runtime_instruction_set.register("MUL", instruction_mul)
        runtime_instruction_set.register("DIV", instruction_div)

        runtime_instruction_set.register("EQ", instruction_eq)
        runtime_instruction_set.register("NE", instruction_ne)
        runtime_instruction_set.register("GT", instruction_gt)

        runtime_instruction_set.register("PIN_MODE", instruction_pin_mode)
        runtime_instruction_set.register("DIGITAL_WRITE", instruction_digital_write)
        runtime_instruction_set.register("DIGITAL_READ", instruction_digital_read)

        cls.initialized = True
