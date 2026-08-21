"""
Runtime PWM do UAP.

Controla valores PWM para motores, LEDs, servos e outros atuadores.
"""


class RuntimePWM:

    def __init__(self):

        self._channels = {}

    def setup(
        self,
        pin,
        frequency=1000,
    ):

        pin = int(pin)

        self._channels[pin] = {
            "frequency": int(frequency),
            "duty": 0,
        }

    def write(
        self,
        pin,
        duty,
    ):

        pin = int(pin)

        if pin not in self._channels:
            self.setup(pin)

        duty = max(
            0,
            min(
                100,
                float(duty),
            ),
        )

        self._channels[pin]["duty"] = duty

        return duty

    def read(
        self,
        pin,
    ):

        channel = self._channels.get(
            int(pin)
        )

        if channel is None:
            return 0

        return channel["duty"]

    def set_frequency(
        self,
        pin,
        frequency,
    ):

        pin = int(pin)

        if pin not in self._channels:
            self.setup(pin)

        self._channels[pin][
            "frequency"
        ] = int(frequency)

    def get_frequency(
        self,
        pin,
    ):

        channel = self._channels.get(
            int(pin)
        )

        if channel is None:
            return 0

        return channel["frequency"]

    def stop(
        self,
        pin,
    ):

        return self.write(
            pin,
            0,
        )

    def reset(self):

        self._channels.clear()

    def all_channels(self):

        return {
            pin: data.copy()
            for pin, data
            in self._channels.items()
        }


runtime_pwm = RuntimePWM()
