from app.modules.uhal.hal_manager import (
    HALManager,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class CountingDriver:

    def __init__(
        self,
        initialize_result=True,
    ):
        self.initialize_calls = 0
        self.shutdown_calls = 0
        self.initialize_result = (
            initialize_result
        )

    def initialize(self):
        self.initialize_calls += 1
        return self.initialize_result

    def shutdown(self):
        self.shutdown_calls += 1
        return True


def test_hal_manager_switches_driver_and_is_idempotent():
    hardware_registry.clear()

    first = CountingDriver()
    second = CountingDriver()

    hardware_registry.register(
        "first",
        first,
    )

    hardware_registry.register(
        "second",
        second,
    )

    manager = HALManager()

    try:
        assert manager.load(
            "FIRST"
        ) is first

        assert manager.load(
            "first"
        ) is first

        assert (
            first.initialize_calls
            == 1
        )

        assert (
            first.shutdown_calls
            == 0
        )

        assert manager.load(
            "second"
        ) is second

        assert (
            first.shutdown_calls
            == 1
        )

        assert (
            second.initialize_calls
            == 1
        )

        assert (
            manager.current_board()
            == "second"
        )

    finally:
        manager.unload()
        hardware_registry.clear()
