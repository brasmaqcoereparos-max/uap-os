import time


class RuntimeClock:

    def now(self):

        return time.time()

    def millis(self):

        return int(

            time.time() * 1000

        )


runtime_clock = RuntimeClock()
