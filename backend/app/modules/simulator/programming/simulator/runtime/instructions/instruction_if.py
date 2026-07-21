from app.modules.simulator.programming.simulator.runtime.instructions.instruction_goto import (
    RuntimeGoto,
)


def instruction_if(

    condition,

    label,

):

    if condition:

        raise RuntimeGoto(

            label,

        )
