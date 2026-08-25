from app.modules.uhal.hal_base import (
    UHALBase,
)

from app.modules.uhal.board_info import (
    BoardInfo,
)


class DriverBase(UHALBase):

    def __init__(
        self,
        board_name,
        manufacturer,
    ):

        self.board = BoardInfo(
            board_name,
            manufacturer,
        )

        self.initialized = False

    def initialize(self):

        self.initialized = True

        return True

    def shutdown(self):

        self.initialized = False

        return True

    def is_initialized(self):

        return self.initialized

    def connect(self):

        return self.initialize()

    def disconnect(self):

        return self.shutdown()

    def update(self):

        return True

    def digital_write(
        self,
        pin,
        value,
    ):

        raise NotImplementedError

    def digital_read(
        self,
        pin,
    ):

        raise NotImplementedError

    def analog_read(
        self,
        pin,
    ):

        raise NotImplementedError

    def analog_write(
        self,
        pin,
        value,
    ):

        raise NotImplementedError

    def pwm_write(
        self,
        pin,
        duty,
    ):

        raise NotImplementedError

    def pwm_frequency(
        self,
        pin,
        frequency,
    ):

        raise NotImplementedError
