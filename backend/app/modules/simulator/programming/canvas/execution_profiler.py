from datetime import datetime


class ExecutionProfiler:

    def __init__(self):

        self.sessions = []

        self.current = None

    def start(self):

        self.current = {
            "started": datetime.now(),
            "finished": None,
            "nodes": [],
        }

    def node(
        self,
        node_id,
        elapsed,
    ):

        if self.current is None:
            return

        self.current["nodes"].append(
            {
                "node": node_id,
                "elapsed": elapsed,
            }
        )

    def finish(self):

        if self.current is None:
            return

        self.current["finished"] = datetime.now()

        self.sessions.append(self.current)

        self.current = None

    def all(self):

        return self.sessions


execution_profiler = ExecutionProfiler()
