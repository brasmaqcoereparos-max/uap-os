import pytest

from app.modules.uhal.driver_loader import (
    DriverLoader,
)

from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class FailingDriver:

    def initialize(self):
        return False

    def shutdown(self):
        return True


def test_driver_loader_rejects_failed_initialization():

    hardware_registry.clear()

    hardware_registry.register(
        "failing",
        FailingDriver(),
    )

    try:

        loader = DriverLoader()

        with pytest.raises(
            RuntimeError
        ):
            loader.load(
                "failing"
            )

    finally:

        hardware_registry.clear()
