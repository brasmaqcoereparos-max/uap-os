import time


class VirtualTimer:

    def __init__(

        self,

        interval,

        callback,

    ):

        self.interval = interval

        self.callback = callback

        self.last = time.time()

    def update(self):

        now = time.time()

        if now - self.last >= self.interval:

            self.last = now

            self.callback()
