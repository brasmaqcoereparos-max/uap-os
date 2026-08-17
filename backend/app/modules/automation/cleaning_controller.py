class CleaningController:

    def __init__(
        self,
        task_manager,
        scheduler,
    ):

        self.task_manager = task_manager
        self.scheduler = scheduler

        self.current_task = None

    def start(self):

        tasks = (
            self.task_manager
            .get_pending()
            .values()
        )

        self.scheduler.load(tasks)
        self.scheduler.start()

        self.current_task = (
            self.scheduler.next_task()
        )

        return self.current_task

    def next(self):

        if self.current_task is not None:

            self.current_task.complete()

        self.current_task = (
            self.scheduler.next_task()
        )

        return self.current_task

    def stop(self):

        self.scheduler.stop()
        self.current_task = None

    def get_current_task(self):

        return self.current_task
