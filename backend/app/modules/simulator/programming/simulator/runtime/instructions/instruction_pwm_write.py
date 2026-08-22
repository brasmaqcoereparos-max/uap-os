"""
Instrução PWM_WRITE do UAP.

Define o duty cycle de um canal PWM.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_pwm_write(
    pin,
    duty,
):
    """
    PWM_WRITE pino, duty
    """

    duty = max(
        0.0,
        min(
            100.0,
            float(duty),
        ),
    )

    return runtime_context.pwm.write(
        int(pin),
        duty,
    )
