"""
Contexto central de execução do UAP.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)

from app.modules.simulator.programming.simulator.runtime.runtime_pwm import (
    runtime_pwm,
)

from app.modules.simulator.programming.simulator.runtime.runtime_timer import (
    runtime_timer,
)

from app.modules.simulator.programming.simulator.runtime.runtime_state import (
    runtime_state,
)

from app.modules.simulator.programming.simulator.runtime.runtime_instruction_set import (
    runtime_instruction_set,
)


class RuntimeContext:

    def __init__(self):

        self.gpio = runtime_gpio
        self.pwm = runtime_pwm
        self.timer = runtime_timer
        self.state = runtime_state
        self.instructions = runtime_instruction_set

    def reset(self):

        self.gpio.reset()
        self.pwm.reset()
        self.timer.reset()
        self.state.reset()


runtime_context = RuntimeContext()
