class VirtualClock:

    def __init__(self):

        self.tick = 0

    def next(self):

        self.tick += 1

    def reset(self):

        self.tick = 0


virtual_clock = VirtualClock()
