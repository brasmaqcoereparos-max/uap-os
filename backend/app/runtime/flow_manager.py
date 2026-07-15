class FlowManager:

    def __init__(self):
        self.flows = {}

    def register(self, flow):
        self.flows[flow.id] = flow

    def unregister(self, flow_id):
        if flow_id in self.flows:
            del self.flows[flow_id]

    def get(self, flow_id):
        return self.flows.get(flow_id)

    def list(self):
        return list(self.flows.values())

    def start_all(self):
        for flow in self.flows.values():
            if hasattr(flow, "start"):
                flow.start()

    def stop_all(self):
        for flow in self.flows.values():
            if hasattr(flow, "stop"):
                flow.stop()

    def execute(self):
        for flow in self.flows.values():
            if hasattr(flow, "execute"):
                flow.execute()


flow_manager = FlowManager()
