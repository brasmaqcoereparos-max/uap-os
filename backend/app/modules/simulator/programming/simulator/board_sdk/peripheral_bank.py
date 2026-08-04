class PeripheralBank:

    def __init__(self):

        self.peripherals = []

    def add(

        self,

        peripheral,

    ):

        self.peripherals.append(peripheral)

    def all(self):

        return self.peripherals.copy()


peripheral_bank = PeripheralBank()
