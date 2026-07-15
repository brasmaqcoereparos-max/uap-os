import threading
import time


class RuntimeEngine:

    def __init__(self):
        self.running = False
        self.thread = None

    def start(self):
        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.loop,
            daemon=True,
        )

        self.thread.start()

    def stop(self):
        self.running = False

    def status(self):
        return {
            "running": self.running,
        }

    def loop(self):
        while self.running:
            self.execute_cycle()
            time.sleep(0.1)

    def execute_cycle(self):
        pass


engine = RuntimeEngine()
