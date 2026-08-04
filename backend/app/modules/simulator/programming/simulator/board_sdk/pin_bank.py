class PinBank:

    def __init__(self):

        self.pins = {}

    def add(

        self,

        pin,

    ):

        self.pins[pin.number] = pin

    def get(

        self,

        number,

    ):

        return self.pins.get(number)

    def all(self):

        return list(self.pins.values())


pin_bank = PinBank()
