class RuntimeADC:

    def __init__(self):

        self.channels = {}

    def set(

        self,

        pin,

        value,

    ):

        value = max(

            0,

            min(

                4095,

                int(value),

            ),

        )

        self.channels[pin] = value

    def read(

        self,

        pin,

    ):

        return self.channels.get(

            pin,

            0,

        )

    def reset(self):

        self.channels.clear()


runtime_adc = RuntimeADC()
