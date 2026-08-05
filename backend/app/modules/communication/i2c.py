from app.modules.communication.interface_base import (
    CommunicationInterface,
)


class I2CInterface(CommunicationInterface):

    def __init__(

        self,

        frequency=100000,

    ):

        super().__init__(

            "I2C",

        )

        self.frequency = frequency

    def set_frequency(

        self,

        frequency,

    ):

        self.frequency = frequency
