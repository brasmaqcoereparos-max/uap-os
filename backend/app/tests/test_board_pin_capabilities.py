from app.modules.simulator.programming.simulator.board_sdk.pin import (
    Pin,
)


def test_pin_capabilities_and_io():
    pin = Pin(
        1,
        "GPIO1",
        modes=[
            "gpio",
            "pwm",
        ],
        direction="output",
    )

    assert pin.supports("PWM") is True

    assert pin.write(1) is True
    assert pin.read() == 1

    assert pin.reserve(
        "motor"
    ) is True

    assert pin.write(0) is False

    assert pin.release(
        "motor"
    ) is True

    assert pin.write(0) is True
    assert pin.read() == 0
