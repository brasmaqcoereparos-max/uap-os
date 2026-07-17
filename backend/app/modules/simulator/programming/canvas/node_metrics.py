from datetime import datetime


class NodeMetrics:

    def __init__(self):

        self.metrics = {}

    def touch(
        self,
        node_id,
    ):

        self.metrics[node_id] = {

            "updated": datetime.now(),

            "executions": self.metrics.get(

                node_id,

                {},

            ).get(

                "executions",

                0,

            ),

        }

    def executed(
        self,
        node_id,
    ):

        self.touch(node_id)

        self.metrics[node_id][

            "executions"

        ] += 1

    def get(
        self,
        node_id,
    ):

        data = self.metrics.get(
            node_id,
        )

        if data is None:

            return None

        return {

            "updated": data["updated"].isoformat(),

            "executions": data["executions"],

        }


node_metrics = NodeMetrics()
