from app.modules.simulator.programming.simulator.board_sdk.peripheral import (
    Peripheral,
)

from app.modules.simulator.programming.simulator.board_sdk.peripheral_bank import (
    PeripheralBank,
)


def test_peripheral_bank_lifecycle():
    bank = PeripheralBank()

    display = Peripheral(
        name="display",
        peripheral_type="display",
        interface="i2c",
        pins=[
            21,
            22,
        ],
        metadata={
            "model": "OLED",
        },
    )

    bank.add(
        display
    )

    assert bank.exists(
        "display"
    ) is True

    assert bank.get(
        "display"
    ) is display

    assert bank.by_type(
        "DISPLAY"
    ) == [
        display
    ]

    initialization = (
        bank.initialize_all()
    )

    assert (
        initialization[
            "display"
        ]
        is True
    )

    assert (
        display.initialized
        is True
    )

    shutdown = (
        bank.shutdown_all()
    )

    assert (
        shutdown[
            "display"
        ]
        is True
    )

    assert (
        display.initialized
        is False
    )

    assert bank.count() == 1
