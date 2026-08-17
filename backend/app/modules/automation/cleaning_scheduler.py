class CleaningScheduler:

    def __init__(self):

        self.tasks = []
        self.active = False

    def load(self, tasks):

        self.tasks = list(tasks)

    def start(self):

        self.active = True

    def stop(self):

        self.active = False

    def next_task(self):

        if not self.active:
            return None

        for task in self.tasks:

            if (
                task.enabled
                and not task.completed
            ):

                return task

        return None

    def is_active(self):

        return self.active
