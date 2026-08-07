class SoftLimits:

    def __init__(self):

        self.enabled = True

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False


soft_limits = SoftLimits()
