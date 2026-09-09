from app.modules.uhal.board_detector import (
    board_detector,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)


class AutoLoader:

    def load(
        self,
        board=None,
    ):

        selected_board = (
            board_detector.detect(
                preferred=board,
            )
        )

        return hal_manager.load(
            selected_board
        )


auto_loader = AutoLoader()
