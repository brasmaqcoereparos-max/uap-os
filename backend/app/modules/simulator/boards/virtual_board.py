class VirtualBoard:

    def __init__(
        self,
        board_id: str,
        name: str,
        board_type: str,
        digital_pins: int,
        analog_pins: int,
    ):
        self.id = board_id
        self.name = name
        self.type = board_type

        self.digital = {
            pin: 0
            for pin in range(digital_pins)
        }

        self.analog = {
            pin: 0
            for pin in range(analog_pins)
        }

    def digital_write(
        self,
        pin: int,
        value: int,
    ):
        self.digital[pin] = value

    def digital_read(
        self,
        pin: int,
    ):
        return self.digital.get(pin, 0)

    def analog_write(
        self,
        pin: int,
        value: float,
    ):
        self.analog[pin] = value

    def analog_read(
        self,
        pin: int,
    ):
        return self.analog.get(pin, 0)

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "digital": self.digital,
            "analog": self.analog,
        }
