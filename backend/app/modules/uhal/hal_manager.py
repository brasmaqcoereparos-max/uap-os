from app.modules.uhal.hardware_registry import (
    hardware_registry,
)


class HALManager:

    def __init__(self):

        self.driver = None
        self.board = None

    def load(
        self,
        board,
    ):

        driver = hardware_registry.get(
            board
        )

        if driver is None:
            raise KeyError(
                f"Driver de hardware '{board}' não encontrado."
            )

        self.board = board
        self.driver = driver

        if hasattr(
            driver,
            "initialize",
        ):

            driver.initialize()

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

    def digital_write(
        self,
        pin,
        value,
    ):

        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL carregado."
            )

        return self.driver.digital_write(
            pin,
            value,
        )

    def digital_read(
        self,
        pin,
    ):

        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL carregado."
            )

        return self.driver.digital_read(
            pin
        )

    def analog_read(
        self,
        pin,
    ):

        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL carregado."
            )

        return self.driver.analog_read(
            pin
        )

    def analog_write(
        self,
        pin,
        value,
    ):

        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL carregado."
            )

        return self.driver.analog_write(
            pin,
            value,
        )

    def pwm_write(
        self,
        pin,
        duty,
    ):

        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL carregado."
            )

        return self.driver.pwm_write(
            pin,
            duty,
        )

    def pwm_frequency(
        self,
        pin,
        frequency,
    ):

        if self.driver is None:
            raise RuntimeError(
                "Nenhum driver UHAL carregado."
            )

        return self.driver.pwm_frequency(
            pin,
            frequency,
        )


hal_manager = HALManager()
