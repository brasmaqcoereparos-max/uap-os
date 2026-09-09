from app.modules.simulator.programming.simulator.boards.board_loader import (
    BoardLoader,
)

from app.modules.simulator.programming.simulator.boards.board_manager import (
    board_manager,
)


def test_board_loader_load_and_reset_lifecycle():
    board_manager.clear()

    BoardLoader.reset()

    board = BoardLoader.load()

    assert (
        board_manager.get_board()
        is board
    )

    assert (
        BoardLoader.status()[
            "loaded"
        ]
        is True
    )

    assert (
        BoardLoader.status()[
            "current"
        ]
        == "Arduino UNO"
    )

    BoardLoader.reset()

    assert (
        BoardLoader.status()[
            "loaded"
        ]
        is False
    )

    assert (
        board_manager.get_board()
        is None
  )
