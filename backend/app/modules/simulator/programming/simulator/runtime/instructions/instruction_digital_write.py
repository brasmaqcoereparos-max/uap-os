from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


def instruction_digital_write(
    pin,
    value,
):

    runtime_gpio.write(
        pin,
        value,
    )
