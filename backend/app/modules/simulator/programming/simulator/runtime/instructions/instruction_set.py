from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


def instruction_set(

    variable,

    value,

):

    runtime_context.variables[

        variable

    ] = value
