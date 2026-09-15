from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.hardware_service import (
    HardwareService,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)


def test_hardware_service_bootstraps_and_resolves_alias():

    hal_manager.unload()

    hardware_registry.clear()

    service = HardwareService()

    try:

        driver = service.load(
            "uno"
        )

        assert (
            driver.board.name
            == "Arduino Uno"
        )

        status = service.status()

        assert (
            status["loaded"]
            is True
        )

        assert (
            status["board"]
            == "arduino_uno"
        )

    finally:

        hal_manager.unload()

        hardware_registry.clear()
