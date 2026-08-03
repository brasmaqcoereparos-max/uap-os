class Interrupt:

    def __init__(

        self,

        pin,

        callback,

    ):

        self.pin = pin

        self.callback = callback

    def trigger(self):

        self.callback()
