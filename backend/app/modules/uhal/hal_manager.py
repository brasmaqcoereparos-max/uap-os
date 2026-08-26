from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class HALManager:

    def __init__(self):
        self.driver = None
        self.board = None

    def load(self, board):
        driver = hardware_registry.get(board)

        if driver is None:
            raise KeyError(
                f"Driver de hardware '{board}' não encontrado."
            )

        self.driver = driver
        self.board = board

        initialize = getattr(
            driver,
            "initialize",
            None,
        )

        if callable(initialize):
            initialize()

        return driver

    def unload(self):
        if self.driver is not None:
            shutdown = getattr(
                self.driver,
                "shutdown",
                None,
            )

            if callable(shutdown):
                shutdown()

        self.driver = None
        self.board = None

    def current(self):
        return self.driver

    def current_board(self):
        return self.board

    def available(self):
        return hardware_registry.all()

    def require_driver(self):
        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL está carregado."
            )

        return self.driver

    def pin_mode(self, pin, mode):
        driver = self.require_driver()

        method = getattr(
            driver,
            "pin_mode",
            None,
        )

        if not callable(method):
            raise AttributeError(
                "Driver não implementa pin_mode()."
            )

        return method(pin, mode)

    def digital_write(self, pin, value):
        driver = self.require_driver()

        return driver.digital_write(
            pin,
            value,
        )

    def digital_read(self, pin):
        driver = self.require_driver()

        return driver.digital_read(pin)

    def analog_write(self, pin, value):
        driver = self.require_driver()

        return driver.analog_write(
            pin,
            value,
        )

    def analog_read(self, pin):
        driver = self.require_driver()

        return driver.analog_read(pin)

    def pwm_write(self, pin, duty):
        driver = self.require_driver()

        return driver.pwm_write(
            pin,
            duty,
        )

    def pwm_frequency(self, pin, frequency):
        driver = self.require_driver()

        return driver.pwm_frequency(
            pin,
            frequency,
        )


hal_manager = HALManager()
