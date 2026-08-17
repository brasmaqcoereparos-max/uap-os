class CleaningTaskManager:

    def __init__(self):

        self.tasks = {}

    def add(self, task):

        self.tasks[
            task.task_id
        ] = task

        return task

    def remove(self, task_id):

        if task_id not in self.tasks:
            return False

        self.tasks.pop(task_id)

        return True

    def get(self, task_id):

        return self.tasks.get(task_id)

    def get_all(self):

        return dict(self.tasks)

    def get_pending(self):

        return {
            task_id: task
            for task_id, task
            in self.tasks.items()
            if not task.completed
            and task.enabled
        }

    def complete(self, task_id):

        task = self.get(task_id)

        if task is None:
            return False

        task.complete()

        return True
