import time


class Tick:

    def __init__(self):

        self.interval = 0.02

    def wait(self):

        time.sleep(self.interval)


tick = Tick()
