class Statistics:

    def __init__(self):

        self.frames = 0

    def frame(self):

        self.frames += 1

    def reset(self):

        self.frames = 0


statistics = Statistics()
