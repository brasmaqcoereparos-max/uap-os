class GPIOController:

    def __init__(self):
        self.initialized = False
        self._pins = {}

    def initialize(self):
        self.initialized = True
        return True

    def shutdown(self):
        self._pins.clear()
        self.initialized = False
        return True

    def setup_output(self, pin, initial=False):
        self._pins[pin] = {
            "mode": "output",
            "value": bool(initial),
        }
        return True

    def setup_input(self, pin, pull_up=False):
        self._pins[pin] = {
            "mode": "input",
            "value": False,
            "pull_up": bool(pull_up),
        }
        return True

    def write(self, pin, value):
        if pin not in self._pins:
            self.setup_output(pin)

        self._pins[pin]["value"] = bool(value)
        return True

    def read(self, pin):
        if pin not in self._pins:
            self.setup_input(pin)

        return int(
            bool(
                self._pins[pin]["value"]
            )
        )

    def cleanup(self, pin=None):
        if pin is None:
            self._pins.clear()
        else:
            self._pins.pop(pin, None)

        return True


gpio_controller = GPIOController()
