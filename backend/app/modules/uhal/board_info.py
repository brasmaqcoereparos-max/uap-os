from app.modules.uhal.board_capabilities import (
    BoardCapabilities,
)


class BoardInfo:

    def __init__(

        self,

        name,

        manufacturer,

    ):

        self.name = name

        self.manufacturer = manufacturer

        self.version = ""

        self.capabilities = BoardCapabilities()
