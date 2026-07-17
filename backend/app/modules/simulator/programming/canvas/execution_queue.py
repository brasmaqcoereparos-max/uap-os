from collections import deque


class ExecutionQueue:

    def __init__(self):

        self.queue = deque()

    def add(
        self,
        node_id,
    ):

        self.queue.append(node_id)

    def next(self):

        if not self.queue:

            return None

        return self.queue.popleft()

    def clear(self):

        self.queue.clear()

    def empty(self):

        return len(self.queue) == 0

    def size(self):

        return len(self.queue)

    def all(self):

        return list(self.queue)


execution_queue = ExecutionQueue()
