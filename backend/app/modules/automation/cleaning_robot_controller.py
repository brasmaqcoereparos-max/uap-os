class CleaningRobotController:

    def __init__(
        self,
        context,
        cycle,
    ):

        self.context = context
        self.cycle = cycle

    def start(self):

        self.context.start()
        self.cycle.start()

    def pause(self):

        self.context.pause()

    def resume(self):

        self.context.resume()

    def stop(self):

        self.cycle.stop()
        self.context.stop()

    def update(
        self,
        distance=None,
    ):

        return self.cycle.update(
            distance
        )

    def get_status(self):

        return self.context.get()
