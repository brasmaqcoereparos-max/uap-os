from app.runtime.driver_base import DriverBase


class ModbusDriver(DriverBase):

    def __init__(
        self,
        driver_id: str,
        name: str,
        host: str,
        port: int = 502,
        unit_id: int = 1,
    ):
        super().__init__(driver_id, name)

        self.host = host
        self.port = port
        self.unit_id = unit_id
        self.client = None

    def connect(self):
        try:
            from pymodbus.client import ModbusTcpClient

            self.client = ModbusTcpClient(
                host=self.host,
                port=self.port,
            )

            self.connected = self.client.connect()

        except Exception:
            self.connected = False

    def disconnect(self):
        if self.client:
            self.client.close()

        self.connected = False

    def update(self):
        if not self.connected:
            return

    def read_holding_registers(
        self,
        address: int,
        count: int = 1,
    ):
        if not self.connected:
            return None

        return self.client.read_holding_registers(
            address=address,
            count=count,
            slave=self.unit_id,
        )

    def write_register(
        self,
        address: int,
        value: int,
    ):
        if not self.connected:
            return None

        return self.client.write_register(
            address=address,
            value=value,
            slave=self.unit_id,
        )
