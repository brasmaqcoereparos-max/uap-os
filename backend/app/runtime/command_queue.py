from queue import Empty, Queue


class CommandQueue:

    def __init__(self):
        self.queue = Queue()

    def put(self, command: dict):
        if not isinstance(command, dict):
            raise TypeError(
                "O comando deve ser um dicionário."
            )

        self.queue.put(command)

    def get(self):
        try:
            return self.queue.get_nowait()
        except Empty:
            return None

    def task_done(self):
        self.queue.task_done()

    def size(self):
        return self.queue.qsize()

    def empty(self):
        return self.queue.empty()

    def clear(self):
        while True:
            try:
                self.queue.get_nowait()
                self.queue.task_done()
            except Empty:
                break


command_queue = CommandQueue()
