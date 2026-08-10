class ParallelExecutor:

    def __init__(self):

        self.tasks = []

    def add(
        self,
        task,
    ):

        self.tasks.append(task)

    def clear(self):

        self.tasks.clear()

    def list_tasks(self):

        return list(self.tasks)
