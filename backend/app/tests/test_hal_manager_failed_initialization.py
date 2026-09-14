import pytest

from app.modules.uhal.hal_manager import (
    HALManager,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class FailingDriver:

    def initialize(self):
        return False

    def shutdown(self):
        return True


def test_failed_driver_is_not_committed_to_hal_manager():
    hardware_registry.clear()

    hardware_registry.register(
        "failing",
        FailingDriver(),
    )

    manager = HALManager()

    try:
        with pytest.raises(
            RuntimeError
        ):
            manager.load(
                "failing"
            )

        assert (
            manager.current()
            is None
        )

        assert (
            manager.current_board()
            is None
        )

    finally:
        manager.unload()
        hardware_registry.clear()
