from app.modules.uhal.board_detector import (
    board_detector,
)

from app.modules.uhal.hal_manager import (
    hal_manager,
)


class AutoLoader:

    def load(self):

        board = board_detector.detect()

        return hal_manager.load(board)


auto_loader = AutoLoader()
