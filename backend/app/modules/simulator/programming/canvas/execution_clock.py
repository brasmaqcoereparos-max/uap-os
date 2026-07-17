import time


class ExecutionClock:

    def __init__(self):

        self.started = None

    def start(self):

        self.started = time.time()

    def millis(self):

        if self.started is None:

            return 0

        return int(

            (time.time() - self.started)

            * 1000

        )

    def seconds(self):

        if self.started is None:

            return 0

        return round(

            time.time() - self.started,

            3,

        )

    def reset(self):

        self.started = None


execution_clock = ExecutionClock()
