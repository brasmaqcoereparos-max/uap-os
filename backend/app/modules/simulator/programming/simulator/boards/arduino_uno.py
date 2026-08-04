from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ArduinoUNO(BoardBase):

    name = "Arduino Uno"

    manufacturer = "Arduino"

    gpio_count = 20

    pwm_count = 6

    adc_count = 6

    flash_size = 32768

    ram_size = 2048

    cpu = "ATmega328P"

    frequency = 16000000
