class NavigationMode:

    MANUAL = "manual"
    TEACH = "teach"
    AUTOMATIC = "automatic"
    VISION = "vision"
    FOLLOW = "follow"
    DOCKING = "docking"

    def __init__(self):

        self.mode = self.MANUAL

    def set(self, mode):

        self.mode = mode

    def get(self):

        return self.mode

    def is_manual(self):

        return self.mode == self.MANUAL

    def is_automatic(self):

        return self.mode == self.AUTOMATIC
