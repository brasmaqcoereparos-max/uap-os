from app.modules.ude.actuator import Actuator


class Valve(Actuator):

    def __init__(
        self,
        name,
    ):

        super().__init__(
            name,
            "valve",
        )

        self.opened = False

    def open(self):

        self.opened = True
        self.set(1)

    def close(self):

        self.opened = False
        self.set(0)

    def is_open(self):

        return self.opened
