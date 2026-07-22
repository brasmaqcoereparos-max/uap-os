from app.modules.simulator.programming.simulator.runtime.runtime_pwm import (
    runtime_pwm,
)


def instruction_pwm_write(

    pin,

    value,

):

    runtime_pwm.write(

        pin,

        value,

    )
