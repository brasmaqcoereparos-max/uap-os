from app.modules.communication.interface_base import (
    CommunicationInterface,
)


class UARTInterface(CommunicationInterface):

    def __init__(

        self,

        baudrate=115200,

    ):

        super().__init__(

            "UART",

        )

        self.baudrate = baudrate

    def set_baudrate(

        self,

        baudrate,

    ):

        self.baudrate = baudrate
