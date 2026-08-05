class LimitSwitch:

    def __init__(

        self,

        name,

    ):

        self.name = name

        self.active = False

    def trigger(self):

        self.active = True

    def reset(self):

        self.active = False

    def is_active(self):

        return self.active
