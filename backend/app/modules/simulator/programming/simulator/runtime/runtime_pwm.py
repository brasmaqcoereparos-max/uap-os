class RuntimePWM:

    def __init__(self):

        self.channels = {}

    def write(

        self,

        pin,

        duty,

    ):

        duty = max(

            0,

            min(

                255,

                int(duty),

            ),

        )

        self.channels[pin] = duty

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


runtime_pwm = RuntimePWM()
