from app.modules.ude.actuator import Actuator


class Relay(Actuator):

    def __init__(
        self,
        name,
    ):

        super().__init__(
            name,
            "relay",
        )

        self.state = False

    def on(self):

        self.state = True
        self.set(True)

    def off(self):

        self.state = False
        self.set(False)

    def toggle(self):

        if self.state:
            self.off()
        else:
            self.on()

    def is_on(self):

        return self.state
