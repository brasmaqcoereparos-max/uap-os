"""
Contexto de execução do UAP.

Centraliza o acesso aos recursos disponíveis durante a execução
de uma automação.
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


class RuntimeContext:

    def __init__(self):

        self.gpio = runtime_gpio
        self.pwm = runtime_pwm
        self.timer = runtime_timer
        self.state = runtime_state

    def reset(self):

        self.gpio.reset()
        self.pwm.reset()
        self.timer.reset()
        self.state.reset()


runtime_context = RuntimeContext()
