import heapq


class RealTimeScheduler:

    def __init__(self):

        self.tasks = []

    def schedule(
        self,
        priority,
        task,
    ):

        heapq.heappush(

            self.tasks,

            (

                priority,

                task,

            ),

        )

    def next(self):

        if not self.tasks:

            return None

        return heapq.heappop(

            self.tasks

        )[1]

    def clear(self):

        self.tasks.clear()

    def size(self):

        return len(self.tasks)


execution_scheduler_rt = RealTimeScheduler()
