from app.modules.uhal.drivers.driver_base import (
    DriverBase,
)


class SimulatorDriver(DriverBase):

    def __init__(self):

        super().__init__(
            "Simulator",
            "Universal Automation Platform",
        )

        self.pins = {}

        self.pwm_frequencies = {}

    def pin_mode(
        self,
        pin,
        mode,
    ):

        self.pins[pin] = {
            "mode": mode,
            "value": 0,
        }

        return True

    def digital_write(
        self,
        pin,
        value,
    ):

        if pin not in self.pins:

            self.pins[pin] = {
                "mode": "output",
                "value": 0,
            }

        self.pins[
            pin
        ][
            "value"
        ] = value

        return True

    def digital_read(
        self,
        pin,
    ):

        return self.pins.get(
            pin,
            {},
        ).get(
            "value",
            0,
        )

    def analog_write(
        self,
        pin,
        value,
    ):

        if pin not in self.pins:

            self.pins[pin] = {
                "mode": "analog",
                "value": 0,
            }

        self.pins[
            pin
        ][
            "value"
        ] = value

        return True

    def analog_read(
        self,
        pin,
    ):

        return self.digital_read(
            pin
        )

    def pwm_write(
        self,
        pin,
        duty,
    ):

        try:

            duty = float(
                duty
            )

        except (
            TypeError,
            ValueError,
        ) as exc:

            raise ValueError(
                "Duty cycle PWM inválido."
            ) from exc

        if duty < 0:
            duty = 0.0

        if duty > 1:
            duty = 1.0

        if pin not in self.pins:

            self.pins[pin] = {
                "mode": "pwm",
                "value": 0.0,
            }

        self.pins[
            pin
        ][
            "mode"
        ] = "pwm"

        self.pins[
            pin
        ][
            "value"
        ] = duty

        return True

    def pwm_frequency(
        self,
        pin,
        frequency,
    ):

        try:

            frequency = float(
                frequency
            )

        except (
            TypeError,
            ValueError,
        ) as exc:

            raise ValueError(
                "Frequência PWM inválida."
            ) from exc

        if frequency <= 0:

            raise ValueError(
                "A frequência PWM "
                "deve ser maior que zero."
            )

        self.pwm_frequencies[
            pin
        ] = frequency

        return True

    def get_pwm_frequency(
        self,
        pin,
        default=None,
    ):

        return self.pwm_frequencies.get(
            pin,
            default,
        )

    def reset_pin(
        self,
        pin,
    ):

        existed = (
            pin in self.pins
            or pin
            in self.pwm_frequencies
        )

        self.pins.pop(
            pin,
            None,
        )

        self.pwm_frequencies.pop(
            pin,
            None,
        )

        return existed

    def reset(self):

        self.pins.clear()

        self.pwm_frequencies.clear()

        return True

    def status(self):

        status = super().status()

        status.update({
            "pins": {
                pin: dict(
                    state
                )
                for pin, state
                in self.pins.items()
            },
            "pwm_frequencies": dict(
                self.pwm_frequencies
            ),
        })

        return status
