class TeachMode:

    def __init__(self):

        self.enabled = False

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def is_enabled(self):

        return self.enabled


teach_mode = TeachMode()
