from collections import deque


class CompilerQueue:

    def __init__(self):

        self.queue = deque()

    def enqueue(
        self,
        item,
    ):

        self.queue.append(item)

    def dequeue(self):

        if not self.queue:

            return None

        return self.queue.popleft()

    def peek(self):

        if not self.queue:

            return None

        return self.queue[0]

    def size(self):

        return len(self.queue)

    def clear(self):

        self.queue.clear()


compiler_queue = CompilerQueue()
