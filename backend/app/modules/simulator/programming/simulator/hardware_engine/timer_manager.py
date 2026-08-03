class TimerManager:

    def __init__(self):

        self.timers = []

    def add(

        self,

        timer,

    ):

        self.timers.append(timer)

    def update(self):

        for timer in self.timers:

            timer.update()

    def clear(self):

        self.timers.clear()


timer_manager = TimerManager()
