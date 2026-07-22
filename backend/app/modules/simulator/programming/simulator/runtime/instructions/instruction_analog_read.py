
from app.modules.simulator.programming.simulator.runtime.runtime_adc import (
    runtime_adc,
)


def instruction_analog_read(

    pin,

):

    return runtime_adc.read(

        pin,

    )
