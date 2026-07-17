from datetime import datetime


class NodeProfiler:

    def __init__(self):

        self.data = {}

    def begin(
        self,
        node_id,
    ):

        self.data[node_id] = {

            "start": datetime.now(),

            "elapsed": 0,

        }

    def finish(
        self,
        node_id,
    ):

        if node_id not in self.data:

            return

        elapsed = (

            datetime.now()

            - self.data[node_id]["start"]

        ).total_seconds()

        self.data[node_id]["elapsed"] = elapsed

    def get(
        self,
        node_id,
    ):

        return self.data.get(node_id)

    def clear(self):

        self.data.clear()


node_profiler = NodeProfiler()
