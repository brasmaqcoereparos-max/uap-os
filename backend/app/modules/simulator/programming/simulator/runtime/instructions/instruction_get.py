from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_get(

    variable,

):

    return runtime_context.variables.get(

        variable,

    )
