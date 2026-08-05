from app.modules.communication.interface_base import (
    CommunicationInterface,
)


class SPIInterface(CommunicationInterface):

    def __init__(

        self,

        frequency=1000000,

    ):

        super().__init__(

            "SPI",

        )

        self.frequency = frequency

    def set_frequency(

        self,

        frequency,

    ):

        self.frequency = frequency
