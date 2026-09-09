from app.modules.uhal.auto_loader import (
    AutoLoader,
)

from app.modules.uhal.board_detector import (
    BoardDetector,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.register_builtin_drivers import (
    register_builtin_drivers,
)


def test_detector_registry_loader_boundary():

    hardware_registry.clear()

    hal_manager.unload()

    try:

        register_builtin_drivers()

        detector = (
            BoardDetector()
        )

        selected = (
            detector.detect(
                "Arduino Nano"
            )
        )

        assert (
            selected
            == "arduino_nano"
        )

        driver = (
            AutoLoader()
            .load(
                "Arduino Nano"
            )
        )

        assert (
            driver
            is hardware_registry.get(
                "arduino_nano"
            )
        )

        assert (
            hal_manager.current_board()
            == "arduino_nano"
        )

        assert (
            driver.initialized
            is True
        )

    finally:

        hal_manager.unload()

        hardware_registry.clear()
