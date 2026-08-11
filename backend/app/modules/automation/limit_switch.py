class LimitSwitch:

    def __init__(self, name):

        self.name = name
        self.triggered = False

    def trigger(self):

        self.triggered = True

    def reset(self):

        self.triggered = False

    def is_triggered(self):

        return self.triggered
