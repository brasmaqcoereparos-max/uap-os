class FeedHold:

    def __init__(self):

        self.active = False

    def enable(self):

        self.active = True

    def disable(self):

        self.active = False


feed_hold = FeedHold()
