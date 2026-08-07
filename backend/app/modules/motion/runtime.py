class MotionRuntime:

    def __init__(self):

        self.running = False

        self.paused = False

    def start(self):

        self.running = True

        self.paused = False

    def stop(self):

        self.running = False

    def pause(self):

        self.paused = True

    def resume(self):

        self.paused = False

    def is_running(self):

        return self.running


motion_runtime = MotionRuntime()
