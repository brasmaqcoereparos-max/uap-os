from app.modules.simulator.programming.simulator.boards.board_base import (
    BoardBase,
)


class ESP32DevKit(BoardBase):

    name = "ESP32 DevKit"

    manufacturer = "Espressif"

    gpio_count = 39

    pwm_count = 16

    adc_count = 18

    flash_size = 4194304

    ram_size = 520192

    cpu = "Xtensa LX6 Dual Core"

    frequency = 240000000
