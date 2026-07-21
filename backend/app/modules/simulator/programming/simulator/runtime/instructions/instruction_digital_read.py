from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


def instruction_digital_read(
    pin,
):

    return runtime_gpio.read(
        pin,
    )
