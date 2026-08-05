from app.modules.communication.interface_base import (
    CommunicationInterface,
)


class RS232Interface(CommunicationInterface):

    def __init__(

        self,

        baudrate=9600,

    ):

        super().__init__(

            "RS232",

        )

        self.baudrate = baudrate

    def set_baudrate(

        self,

        baudrate,

    ):

        self.baudrate = baudrate
