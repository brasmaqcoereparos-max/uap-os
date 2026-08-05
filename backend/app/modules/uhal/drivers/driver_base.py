from app.modules.uhal.hal_base import HALBase
from app.modules.uhal.board_info import BoardInfo


class DriverBase(HALBase):

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

    def shutdown(self):

        self.initialized = False

    def is_initialized(self):

        return self.initialized
