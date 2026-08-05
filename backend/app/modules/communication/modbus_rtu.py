from app.modules.communication.rs485 import (
    RS485Interface,
)


class ModbusRTU(RS485Interface):

    def __init__(

        self,

        slave_id=1,

    ):

        super().__init__()

        self.slave_id = slave_id

    def read_register(

        self,

        address,

    ):

        return None

    def write_register(

        self,

        address,

        value,

    ):

        pass
