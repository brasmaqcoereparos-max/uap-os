from app.modules.uhal.hal_base import (
    UHALBase,
)

from app.modules.uhal.board_info import (
    BoardInfo,
)


class DriverBase(UHALBase):

    def __init__(
        self,
        board_name,
        manufacturer,
    ):

        self.board = BoardInfo(
            board_name,
            manufacturer,
        )

        self.initialized = False

    def initialize(self):

        self.initialized = True

        return True

    def shutdown(self):

        self.initialized = False

        return True

    def is_initialized(self):

        return self.initialized
