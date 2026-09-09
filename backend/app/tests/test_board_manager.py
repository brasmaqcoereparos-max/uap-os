from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)

from app.modules.simulator.programming.simulator.boards.board_manager import (
    BoardManager,
)


class TestBoard(
    BoardBase
):
    name = "TestBoard"
    manufacturer = "UAP"

    cpu = "simulator"
    architecture = "virtual"

    gpio_count = 20
    pwm_count = 8
    adc_count = 6

    flash_size = 4194304
    ram_size = 520000

    frequency = 240000000
    voltage = 3.3


def test_board_manager_lifecycle():
    manager = (
        BoardManager()
    )

    board = TestBoard(
        board_id="board-1"
    )

    manager.add_board(
        board
    )

    assert manager.exists(
        "board-1"
    ) is True

    selected = manager.select(
        "board-1"
    )

    assert selected is board

    assert manager.has_board() is True

    assert manager.get_board() is board

    assert manager.initialize_current() is True

    assert board.initialized is True
    assert board.running is True

    assert manager.shutdown_current() is True

    assert board.initialized is False
    assert board.running is False
