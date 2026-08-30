"""
Placas virtuais da camada pública do simulador UAP.

Esta camada é utilizada pelo SimulatorService para criação
rápida de placas virtuais.

Ela é distinta do Board SDK interno localizado em:

    simulator/programming/simulator/boards/

A separação é preservada para não quebrar os contratos
existentes do projeto.
"""

from app.modules.simulator.boards.virtual_board import (
    VirtualBoard,
)

from app.modules.simulator.boards.arduino_uno import (
    ArduinoUNO,
)

from app.modules.simulator.boards.esp32 import (
    ESP32Board,
)

from app.modules.simulator.boards.raspberry_pi import (
    RaspberryPiBoard,
)


__all__ = [
    "VirtualBoard",
    "ArduinoUNO",
    "ESP32Board",
    "RaspberryPiBoard",
]
