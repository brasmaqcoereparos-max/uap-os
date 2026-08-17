class CleaningRobotContext:

    def __init__(self):

        self.mode = "idle"
        self.current_area = None
        self.current_task = None
        self.running = False
        self.paused = False

    def start(self):

        self.running = True
        self.paused = False
        self.mode = "cleaning"

    def pause(self):

        self.paused = True
        self.mode = "paused"

    def resume(self):

        self.paused = False
        self.mode = "cleaning"

    def stop(self):

        self.running = False
        self.paused = False
        self.mode = "idle"

    def set_area(self, area):

        self.current_area = area

    def set_task(self, task):

        self.current_task = task

    def get(self):

        return {
            "mode": self.mode,
            "area": self.current_area,
            "task": self.current_task,
            "running": self.running,
            "paused": self.paused,
        }
