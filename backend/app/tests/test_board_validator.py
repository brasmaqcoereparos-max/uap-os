from app.modules.simulator.programming.simulator.board_sdk.board_description import (
    BoardDescription,
)

from app.modules.simulator.programming.simulator.board_sdk.board_validator import (
    BoardValidator,
)


def test_board_validator_accepts_valid_board():
    board = BoardDescription(
        name="ESP32",
        manufacturer="Espressif",
        cpu="Xtensa",
    )

    validator = (
        BoardValidator()
    )

    result = (
        validator.validate_detailed(
            board
        )
    )

    assert result[
        "valid"
    ] is True

    assert result[
        "errors"
    ] == []
