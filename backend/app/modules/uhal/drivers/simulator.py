from app.modules.uhal.hal_base import HALBase


class SimulatorDriver(HALBase):

    def __init__(self):

        self.pins = {}

    def pin_mode(

        self,

        pin,

        mode,

    ):

        self.pins[pin] = {

            "mode": mode,

            "value": 0,

        }

    def digital_write(

        self,

        pin,

        value,

    ):

        if pin in self.pins:

            self.pins[pin]["value"] = value

    def digital_read(

        self,

        pin,

    ):

        return self.pins.get(

            pin,

            {},

        ).get(

            "value",

            0,

        )

    def analog_write(

        self,

        pin,

        value,

    ):

        self.digital_write(

            pin,

            value,

        )

    def analog_read(

        self,

        pin,

    ):

        return self.digital_read(

            pin,

      )
