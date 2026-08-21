"""
Runtime GPIO do UAP.

Camada de abstração para leitura e escrita de pinos digitais.
Funciona como simulador e pode posteriormente ser conectada ao
hardware físico do UAP Box.
"""


class RuntimeGPIO:

    HIGH = 1
    LOW = 0

    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    INPUT_PULLUP = "INPUT_PULLUP"

    def __init__(self):

        self._modes = {}
        self._states = {}

    def setup(
        self,
        pin,
        mode,
        initial=LOW,
    ):

        pin = int(pin)

        self._modes[pin] = mode

        if mode == self.OUTPUT:
            self._states[pin] = (
                self.HIGH
                if initial
                else self.LOW
            )

        elif pin not in self._states:
            self._states[pin] = self.LOW

    def write(
        self,
        pin,
        value,
    ):

        pin = int(pin)

        if pin not in self._modes:
            self.setup(
                pin,
                self.OUTPUT,
            )

        self._states[pin] = (
            self.HIGH
            if bool(value)
            else self.LOW
        )

        return self._states[pin]

    def read(
        self,
        pin,
    ):

        pin = int(pin)

        return self._states.get(
            pin,
            self.LOW,
        )

    def mode(
        self,
        pin,
    ):

        return self._modes.get(pin)

    def toggle(
        self,
        pin,
    ):

        current = self.read(pin)

        return self.write(
            pin,
            not current,
        )

    def reset(self):

        self._modes.clear()
        self._states.clear()

    def all_states(self):

        return self._states.copy()

    def all_modes(self):

        return self._modes.copy()


runtime_gpio = RuntimeGPIO()
