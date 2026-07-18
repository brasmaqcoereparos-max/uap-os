from enum import Enum


class CompilerTarget(Enum):

    ARDUINO = "arduino"

    ESP32 = "esp32"

    RASPBERRY_PI_PICO = "raspberry_pi_pico"

    STM32 = "stm32"

    PYTHON = "python"

    MICROPYTHON = "micropython"

    CPP = "cpp"

    LADDER = "ladder"

    JSON = "json"

    FLOWCHART = "flowchart"
