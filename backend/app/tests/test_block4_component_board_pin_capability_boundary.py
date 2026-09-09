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
    board = UniversalDevice(
        device_id="esp32",
        name="ESP32",
        device_type="board",
        manufacturer="Espressif",
        model="DevKit",
    )

    board.add_capability(
        "gpio",
        {
            "count": 30,
        },
    )

    board.add_capability(
        "pwm",
        {
            "channels": 16,
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
        capabilities=[
            "gpio",
            "pwm",
        ],
        metadata={
            "voltage": 3.3,
        },
    )

    required_capabilities = [
        "gpio",
        "pwm",
    ]

    compatibility = (
        HardwareCompatibilityChecker()
        .check(
            board,
            required_capabilities,
        )
    )

    assert (
        compatibility.compatible
        is True
    )

    assert (
        compatibility.missing_capabilities
        == []
    )

    assert pin.supports(
        "gpio"
    ) is True

    assert pin.supports(
        "pwm"
    ) is True

    assert (
        pin.metadata[
            "voltage"
        ]
        == 3.3
    )

    assert pin.write(
        1
    ) is True

    assert pin.read() == 1

    board_data = board.to_dict()

    assert (
        board_data[
            "device_type"
        ]
        == "board"
    )

    capability_names = {
        capability[
            "name"
        ]
        for capability
        in board_data[
            "capabilities"
        ]
    }

    assert capability_names == {
        "gpio",
        "pwm",
    }
