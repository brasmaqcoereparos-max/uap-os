from app.modules.simulator.boards.virtual_board import VirtualBoard


class ArduinoUNO(VirtualBoard):

    def __init__(
        self,
        board_id: str,
        name: str,
    ):
        super().__init__(
            board_id=board_id,
            name=name,
            board_type="Arduino UNO",
            digital_pins=14,
            analog_pins=6,
        )
