class InterruptManager:

    def __init__(self):

        self.interrupts = {}

    def register(

        self,

        pin,

        callback,

    ):

        self.interrupts[pin] = callback

    def trigger(

        self,

        pin,

    ):

        callback = self.interrupts.get(pin)

        if callback:

            callback()

    def clear(self):

        self.interrupts.clear()


interrupt_manager = InterruptManager()
