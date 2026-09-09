from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.board_sdk.pin import (
    Pin,
)

from app.modules.uhal.compatibility import (
    HardwareCompatibilityChecker,
)

from app.modules.uhal.device_model import (
    UniversalDevice,
)


def test_block4_component_board_pin_capability_boundary():

    component = Component(
        name="Servo",
        component_type="actuator",
        metadata={
            "required_capabilities": [
                "gpio",
                "pwm",
            ],
        },
    )

    pin = Pin(
        number=18,
        name="GPIO18",
        modes=[
            "gpio",
            "pwm",
        ],
        direction="output",
    )

    board = UniversalDevice(
        device_id="esp32",
        name="ESP32",
        device_type="board",
    )

    board.add_capability(
        "gpio"
    )

    board.add_capability(
        "pwm"
    )

    result = (
        HardwareCompatibilityChecker()
        .check(
            board,
            component.get_metadata(
                "required_capabilities"
            ),
        )
    )

    assert (
        pin.supports(
            "gpio"
        )
        is True
    )

    assert (
        pin.supports(
            "pwm"
        )
        is True
    )

    assert (
        result.compatible
        is True
    )

    assert (
        result.missing_capabilities
        == []
  )
