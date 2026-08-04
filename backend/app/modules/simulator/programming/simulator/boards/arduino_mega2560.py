from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ArduinoMega2560(BoardBase):

    name = "Arduino Mega 2560"

    manufacturer = "Arduino"

    gpio_count = 70

    pwm_count = 15

    adc_count = 16

    flash_size = 262144

    ram_size = 8192

    cpu = "ATmega2560"

    frequency = 16000000
