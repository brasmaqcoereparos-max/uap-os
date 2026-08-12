class JogMode:

    def __init__(self):

        self.active = False

    def enable(self):

        self.active = True

    def disable(self):

        self.active = False

    def toggle(self):

        self.active = not self.active

    def is_active(self):

        return self.active


jog_mode = JogMode()
