from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class BoardTemplate(BoardBase):

    name = "New Board"

    manufacturer = "Manufacturer"

    cpu = "CPU"

    frequency = 0

    flash_size = 0

    ram_size = 0

    gpio_count = 0

    pwm_count = 0

    adc_count = 0
