from app.modules.simulator.boards.virtual_board import VirtualBoard


class RaspberryPiBoard(VirtualBoard):

    def __init__(
        self,
        board_id: str,
        name: str,
    ):
        super().__init__(
            board_id=board_id,
            name=name,
            board_type="Raspberry Pi",
            digital_pins=40,
            analog_pins=0,
        )
