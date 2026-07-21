class RuntimeGPIO:

    def __init__(self):

        self.digital = {}

        self.pin_mode = {}

    def mode(
        self,
        pin,
        mode,
    ):

        self.pin_mode[pin] = mode

    def write(
        self,
        pin,
        value,
    ):

        self.digital[pin] = bool(value)

    def read(
        self,
        pin,
    ):

        return self.digital.get(pin, False)

    def reset(self):

        self.digital.clear()

        self.pin_mode.clear()


runtime_gpio = RuntimeGPIO()
