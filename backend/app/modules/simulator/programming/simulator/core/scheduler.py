class Scheduler:

    def __init__(self):

        self.tasks = []

    def add(

        self,

        task,

    ):

        self.tasks.append(task)

    def execute(self):

        for task in self.tasks:

            task()

    def clear(self):

        self.tasks.clear()


scheduler = Scheduler()
