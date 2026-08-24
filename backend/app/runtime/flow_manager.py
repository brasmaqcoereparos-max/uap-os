"""
Gerenciador de flows do Runtime UAP.
"""


class FlowManager:

    def __init__(self):
        self.flows = {}

    def register(self, flow):
        if flow is None:
            raise ValueError(
                "Flow não informado."
            )

        flow_id = getattr(
            flow,
            "id",
            None,
        )

        if flow_id is None:
            raise ValueError(
                "Flow sem id."
            )

        self.flows[flow_id] = flow

        return flow

    def unregister(self, flow_id):
        return self.flows.pop(
            flow_id,
            None,
        )

    def get(self, flow_id):
        return self.flows.get(
            flow_id
        )

    def list(self):
        return list(
            self.flows.values()
        )

    def start_all(self):

        results = {}

        for flow_id, flow in list(
            self.flows.items()
        ):

            start = getattr(
                flow,
                "start",
                None,
            )

            if callable(start):

                try:
                    results[flow_id] = start()

                except Exception as exc:
                    results[flow_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def stop_all(self):

        results = {}

        for flow_id, flow in list(
            self.flows.items()
        ):

            stop = getattr(
                flow,
                "stop",
                None,
            )

            if callable(stop):

                try:
                    results[flow_id] = stop()

                except Exception as exc:
                    results[flow_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def execute(self):

        results = {}

        for flow_id, flow in list(
            self.flows.items()
        ):

            execute = getattr(
                flow,
                "execute",
                None,
            )

            if callable(execute):

                try:
                    results[flow_id] = execute()

                except Exception as exc:
                    results[flow_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def clear(self):
        self.flows.clear()

    def count(self):
        return len(
            self.flows
        )


flow_manager = FlowManager()
