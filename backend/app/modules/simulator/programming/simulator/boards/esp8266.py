from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ESP8266(BoardBase):

    name = "ESP8266"

    manufacturer = "Espressif"

    gpio_count = 17

    pwm_count = 8

    adc_count = 1

    flash_size = 4194304

    ram_size = 81920

    cpu = "Tensilica L106"

    frequency = 80000000
