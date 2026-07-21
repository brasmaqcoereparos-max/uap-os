
from app.modules.simulator.programming.simulator.runtime.runtime_gpio import (
    runtime_gpio,
)


def instruction_pin_mode(
    pin,
    mode,
):

    runtime_gpio.mode(
        pin,
        mode,
    )
