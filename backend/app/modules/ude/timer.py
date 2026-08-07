import time


class DeviceTimer:

    def __init__(self):

        self.started = False
        self.start_time = None

    def start(self):

        self.started = True
        self.start_time = time.time()

    def stop(self):

        self.started = False

    def elapsed(self):

        if not self.started:
            return 0

        return time.time() - self.start_time

    def expired(
        self,
        duration,
    ):

        return self.elapsed() >= duration
