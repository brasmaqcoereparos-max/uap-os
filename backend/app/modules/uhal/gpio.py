from app.modules.uhal.constants import (
    INPUT,
    OUTPUT,
    INPUT_PULLUP,
    INPUT_PULLDOWN,
    HIGH,
    LOW,
    PWM,
    ANALOG,
)

from app.modules.uhal.gpio_manager import (
    gpio_manager,
)


class GPIO:

    INPUT = INPUT

    OUTPUT = OUTPUT

    INPUT_PULLUP = INPUT_PULLUP

    INPUT_PULLDOWN = INPUT_PULLDOWN

    HIGH = HIGH

    LOW = LOW

    PWM = PWM

    ANALOG = ANALOG

    @staticmethod
    def pin_mode(

        pin,

        mode,

    ):

        gpio_manager.pin_mode(

            pin,

            mode,

        )

    @staticmethod
    def digital_write(

        pin,

        value,

    ):

        gpio_manager.digital_write(

            pin,

            value,

        )

    @staticmethod
    def digital_read(

        pin,

    ):

        return gpio_manager.digital_read(

            pin,

        )

    @staticmethod
    def analog_write(

        pin,

        value,

    ):

        gpio_manager.analog_write(

            pin,

            value,

        )

    @staticmethod
    def analog_read(

        pin,

    ):

        return gpio_manager.analog_read(

            pin,

        )
