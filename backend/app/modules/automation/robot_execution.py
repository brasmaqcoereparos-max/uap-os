class RobotExecution:

    def __init__(self):

        self.running = False
        self.paused = False

    def start(self):

        self.running = True
        self.paused = False

    def pause(self):

        if self.running:
            self.paused = True

    def resume(self):

        if self.running:
            self.paused = False

    def stop(self):

        self.running = False
        self.paused = False

    def is_running(self):

        return self.running

    def is_paused(self):

        return self.paused
