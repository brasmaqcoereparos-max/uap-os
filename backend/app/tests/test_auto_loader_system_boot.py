from app.modules.uhal import (
    system_boot,
)

from app.modules.uhal.auto_loader import (
    AutoLoader,
)

from app.modules.uhal.drivers.simulator import (
    SimulatorDriver,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class CountingDriver:

    def __init__(self):

        self.initialize_calls = 0

    def initialize(self):

        self.initialize_calls += 1

        return True

    def shutdown(self):

        return True


def test_auto_loader_resolves_alias_and_loads_driver():

    hardware_registry.clear()

    hal_manager.unload()

    driver = SimulatorDriver()

    hardware_registry.register(
        "arduino_uno",
        driver,
    )

    try:

        loaded = (
            AutoLoader()
            .load(
                "uno"
            )
        )

        assert (
            loaded
            is driver
        )

        assert (
            hal_manager.current_board()
            == "arduino_uno"
        )

        assert (
            driver.initialized
            is True
        )

    finally:

        hal_manager.unload()

        hardware_registry.clear()


def test_system_boot_initializes_selected_driver_once(
    monkeypatch,
):

    driver = (
        CountingDriver()
    )

    def fake_register():

        hardware_registry.clear()

        hardware_registry.register(
            "simulator",
            driver,
        )

        return (
            hardware_registry.all()
        )

    monkeypatch.setattr(
        system_boot,
        "register_builtin_drivers",
        fake_register,
    )

    hal_manager.unload()

    try:

        loaded = (
            system_boot
            .initialize_hardware(
                board="simulator"
            )
        )

        assert (
            loaded
            is driver
        )

        assert (
            driver.initialize_calls
            == 1
        )

        assert (
            hal_manager.current_board()
            == "simulator"
        )

    finally:

        hal_manager.unload()

        hardware_registry.clear()
