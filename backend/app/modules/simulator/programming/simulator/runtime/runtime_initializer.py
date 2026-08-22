"""
Inicialização central do runtime do UAP.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_instruction_set import (
    runtime_instruction_set,
)

from app.modules.simulator.programming.simulator.runtime.instructions.instruction_mov import (
    instruction_mov,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_set import (
    instruction_set,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_get import (
    instruction_get,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_wait import (
    instruction_wait,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_label import (
    instruction_label,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_goto import (
    instruction_goto,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_if import (
    instruction_if,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_call import (
    instruction_call,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_return import (
    instruction_return,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_add import (
    instruction_add,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_sub import (
    instruction_sub,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_mul import (
    instruction_mul,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_div import (
    instruction_div,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_eq import (
    instruction_eq,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_ne import (
    instruction_ne,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_gt import (
    instruction_gt,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_pin_mode import (
    instruction_pin_mode,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_digital_write import (
    instruction_digital_write,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_digital_read import (
    instruction_digital_read,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_pwm_write import (
    instruction_pwm_write,
)
from app.modules.simulator.programming.simulator.runtime.instructions.instruction_analog_read import (
    instruction_analog_read,
)


class RuntimeInitializer:

    initialized = False

    @classmethod
    def initialize(cls):

        if cls.initialized:
            return

        instructions = {
            "MOV": instruction_mov,
            "SET": instruction_set,
            "GET": instruction_get,
            "WAIT": instruction_wait,
            "LABEL": instruction_label,
            "GOTO": instruction_goto,
            "IF": instruction_if,
            "CALL": instruction_call,
            "RETURN": instruction_return,
            "ADD": instruction_add,
            "SUB": instruction_sub,
            "MUL": instruction_mul,
            "DIV": instruction_div,
            "EQ": instruction_eq,
            "NE": instruction_ne,
            "GT": instruction_gt,
            "PIN_MODE": instruction_pin_mode,
            "DIGITAL_WRITE": instruction_digital_write,
            "DIGITAL_READ": instruction_digital_read,
            "PWM_WRITE": instruction_pwm_write,
            "ANALOG_READ": instruction_analog_read,
        }

        for name, instruction in instructions.items():
            runtime_instruction_set.register(
                name,
                instruction,
            )

        cls.initialized = True

    @classmethod
    def reset(cls):

        cls.initialized = False
