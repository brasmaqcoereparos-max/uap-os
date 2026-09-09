from app.modules.simulator.programming.simulator.boards.arduino_uno import (
    ArduinoUNO,
)

from app.modules.simulator.programming.simulator.boards.esp32 import (
    ESP32Board,
)

from app.modules.simulator.programming.simulator.boards.raspberry_pi import (
    RaspberryPiBoard,
)


def test_builtin_board_capabilities_are_exposed():
    uno = ArduinoUNO()

    esp = ESP32Board()

    pi = RaspberryPiBoard()

    assert (
        uno.capabilities()[
            "logic_voltage"
        ]
        == 5.0
    )

    assert (
        esp.capabilities()[
            "wifi"
        ]
        is True
    )

    assert (
        esp.capabilities()[
            "bluetooth"
        ]
        is True
    )

    assert (
        pi.capabilities()[
            "adc_native"
        ]
        is False
    )

    assert (
        pi.capabilities()[
            "logic_voltage"
        ]
        == 3.3
    )
