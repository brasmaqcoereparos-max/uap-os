from app.modules.uhal.hardware_controller import (
    HardwareController,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)


def test_hardware_controller_dispatches_runtime_commands():

    hal_manager.unload()

    hardware_registry.clear()

    controller = (
        HardwareController()
    )

    try:

        status = controller.execute({
            "action": (
                "hardware.initialize"
            ),
            "board": "simulator",
        })

        assert (
            status["loaded"]
            is True
        )

        result = controller.execute({
            "action": "gpio.write",
            "pin": 1,
            "value": 1,
        })

        assert result is True

        value = controller.execute({
            "action": "gpio.read",
            "pin": 1,
        })

        assert value == 1

    finally:

        controller.shutdown()

        hardware_registry.clear()
