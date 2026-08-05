from app.modules.communication.interface_base import (
    CommunicationInterface,
)


class CANBusInterface(CommunicationInterface):

    def __init__(

        self,

        bitrate=500000,

    ):

        super().__init__(

            "CAN",

        )

        self.bitrate = bitrate

    def set_bitrate(

        self,

        bitrate,

    ):

        self.bitrate = bitrate

    def send(

        self,

        can_id,

        data,

    ):

        pass

    def receive(self):

        return None
