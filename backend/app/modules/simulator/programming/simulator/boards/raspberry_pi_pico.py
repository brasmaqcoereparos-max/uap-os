from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class RaspberryPiPico(BoardBase):

    name = "Raspberry Pi Pico"

    manufacturer = "Raspberry Pi"

    gpio_count = 30

    pwm_count = 16

    adc_count = 4

    flash_size = 2097152

    ram_size = 270336

    cpu = "RP2040 Dual Core"

    frequency = 133000000
