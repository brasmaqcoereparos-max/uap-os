"""
UAP Simulator.

Camada pública de simulação da Universal Automation Platform.

Fluxo principal:

    API
     │
     ▼
SimulatorService
     │
     ├── Virtual Boards
     ├── Virtual Devices
     └── Virtual Sensors

O simulador avançado de programação permanece em:

    app.modules.simulator.programming.simulator

Não existe fusão automática entre essas duas camadas.
A integração completa será tratada no bloco de integração
e testes para preservar os contratos atuais.
"""

from app.modules.simulator.service import (
    SimulatorService,
    simulator_service,
)

from app.modules.simulator.devices import (
    VirtualDevice,
    VirtualLED,
    VirtualButton,
    VirtualRelay,
)

from app.modules.simulator.components import (
    VirtualSensor,
    VirtualTemperature,
    VirtualHumidity,
    VirtualUltrasonic,
)

from app.modules.simulator.boards import (
    VirtualBoard,
    ArduinoUNO,
    ESP32Board,
    RaspberryPiBoard,
)


__all__ = [
    "SimulatorService",
    "simulator_service",
    "VirtualDevice",
    "VirtualLED",
    "VirtualButton",
    "VirtualRelay",
    "VirtualSensor",
    "VirtualTemperature",
    "VirtualHumidity",
    "VirtualUltrasonic",
    "VirtualBoard",
    "ArduinoUNO",
    "ESP32Board",
    "RaspberryPiBoard",
]
