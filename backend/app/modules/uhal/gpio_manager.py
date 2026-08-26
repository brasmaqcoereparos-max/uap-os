from app.modules.uhal.hal_manager import (
    hal_manager,
)


class GPIOManager:

    def pin_mode(self, pin, mode):
        return hal_manager.pin_mode(
            pin,
            mode,
        )

    def digital_write(self, pin, value):
        return hal_manager.digital_write(
            pin,
            value,
        )

    def digital_read(self, pin):
        return hal_manager.digital_read(
            pin
        )

    def analog_write(self, pin, value):
        return hal_manager.analog_write(
            pin,
            value,
        )

    def analog_read(self, pin):
        return hal_manager.analog_read(
            pin
        )

    def pwm_write(self, pin, duty):
        return hal_manager.pwm_write(
            pin,
            duty,
        )

    def pwm_frequency(
        self,
        pin,
        frequency,
    ):
        return hal_manager.pwm_frequency(
            pin,
            frequency,
        )


gpio_manager = GPIOManager()
