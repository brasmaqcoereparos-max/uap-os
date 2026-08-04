from app.modules.simulator.programming.simulator.boards.board_manager import (
    board_manager,
)

from app.modules.simulator.programming.simulator.boards.arduino_uno import (
    ArduinoUNO,
)

from app.modules.simulator.programming.simulator.boards.arduino_mega2560 import (
    ArduinoMega2560,
)

from app.modules.simulator.programming.simulator.boards.esp32_devkit import (
    ESP32DevKit,
)

from app.modules.simulator.programming.simulator.boards.esp8266 import (
    ESP8266,
)

from app.modules.simulator.programming.simulator.boards.raspberry_pi_pico import (
    RaspberryPiPico,
)


class BoardLoader:

    loaded = False

    boards = {
        "arduino_uno": ArduinoUNO,
        "arduino_mega2560": ArduinoMega2560,
        "esp32_devkit": ESP32DevKit,
        "esp8266": ESP8266,
        "raspberry_pi_pico": RaspberryPiPico,
    }

    @classmethod
    def load(cls):

        if cls.loaded:
            return

        board_manager.set_board(
            ArduinoUNO(),
        )

        cls.loaded = True

    @classmethod
    def create(
        cls,
        board_name,
    ):

        board = cls.boards.get(board_name)

        if board is None:
            raise ValueError(
                f"Placa '{board_name}' não encontrada."
            )

        return board()
