from app.modules.simulator.programming.simulator.boards.board_manager import (
    board_manager,
)

from app.modules.simulator.programming.simulator.boards.arduino_uno import (
    ArduinoUNO,
)


class BoardLoader:

    loaded = False

    @classmethod
    def load(cls):

        if cls.loaded:

            return

        board_manager.set_board(

            ArduinoUNO(),

        )

        cls.loaded = True
