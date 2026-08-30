"""
Virtual Board Layer (VBL) do UAP.

Contém as placas eletrônicas disponíveis
para uso pelo simulador e pelo Board SDK.
"""

from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
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

from app.modules.simulator.programming.simulator.boards.board_manager import (
    BoardManager,
    board_manager,
)

from app.modules.simulator.programming.simulator.boards.board_loader import (
    BoardLoader,
)


__all__ = [
    "BoardBase",
    "ArduinoUNO",
    "ArduinoMega2560",
    "ESP32DevKit",
    "ESP8266",
    "RaspberryPiPico",
    "BoardManager",
    "board_manager",
    "BoardLoader",
]
