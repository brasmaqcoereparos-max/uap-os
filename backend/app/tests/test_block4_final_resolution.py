from app.modules.simulator.programming.simulator.boards.board_loader import (
    BoardLoader,
)

from app.modules.uhal.compatibility import (
    HardwareCompatibilityChecker,
)

from app.modules.uhal.device_model import (
    UniversalDevice,
)


def test_board4_resolution_to_hardware_capabilities():
    simulated = BoardLoader.create(
        "esp32"
    )

    capabilities = (
        simulated.capabilities()
    )

    device = UniversalDevice(
        device_id=simulated.id,
        name=simulated.name,
        device_type="board",
    )

    required = (
        "gpio",
        "pwm",
        "wifi",
        "bluetooth",
    )

    for name in required:
        if (
            name in (
                "gpio",
                "pwm",
            )
            or capabilities.get(
                name
            )
        ):
            device.add_capability(
                name
            )

    result = (
        HardwareCompatibilityChecker()
        .check(
            device,
            list(required),
        )
    )

    assert (
        result.compatible
        is True
    )

    assert (
        result.missing_capabilities
        == []
          )
