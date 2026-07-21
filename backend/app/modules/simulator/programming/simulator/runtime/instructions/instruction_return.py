from app.modules.simulator.programming.simulator.runtime.runtime_stack import (
    runtime_stack,
)


def instruction_return():

    return runtime_stack.pop()
