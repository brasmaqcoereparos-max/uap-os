from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.uhal.compatibility import (
    HardwareCompatibilityChecker,
)

from app.modules.uhal.device_model import (
    UniversalDevice,
)


def test_component_metadata_requirements_flow_to_hardware_check():
    component = Component(
        name="Servo",
        metadata={
            "required_capabilities": [
                "gpio",
                "pwm",
            ],
            "icon": "servo.svg",
        },
    )

    board = UniversalDevice(
        device_id="b1",
        name="Board",
        device_type="board",
    )

    board.add_capability(
        "gpio"
    )

    board.add_capability(
        "pwm"
    )

    requirements = (
        component.get_metadata(
            "required_capabilities"
        )
    )

    result = (
        HardwareCompatibilityChecker()
        .check(
            board,
            requirements,
        )
    )

    assert result.compatible is True

    assert (
        component.get_metadata(
            "icon"
        )
        == "servo.svg"
    )
