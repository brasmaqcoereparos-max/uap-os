import pytest

from app.modules.uhal.hardware_controller import (
    HardwareController,
)


def test_hardware_controller_rejects_missing_action():

    controller = (
        HardwareController()
    )

    with pytest.raises(
        ValueError
    ):
        controller.execute(
            {}
        )


def test_hardware_controller_rejects_unknown_action():

    controller = (
        HardwareController()
    )

    with pytest.raises(
        ValueError
    ):
        controller.execute({
            "action": (
                "hardware.unknown"
            ),
        })
