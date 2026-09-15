from app.modules.uhal.hardware_registry import (
    hardware_registry,
)

from app.modules.uhal.hardware_service import (
    HardwareService,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)


def test_hardware_service_uses_detector_default(
    monkeypatch,
):

    hal_manager.unload()

    hardware_registry.clear()

    monkeypatch.delenv(
        "UAP_BOARD",
        raising=False,
    )

    monkeypatch.delenv(
        "UAP_BOARD_TYPE",
        raising=False,
    )

    service = HardwareService()

    try:

        driver = service.load(
            None
        )

        assert (
            driver.board.name
            == "Simulator"
        )

        assert (
            service.status()[
                "loaded"
            ]
            is True
        )

    finally:

        hal_manager.unload()

        hardware_registry.clear()
