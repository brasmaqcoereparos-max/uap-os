from app.modules.vision.automation.automation_flow import (
    AutomationFlow,
)


class AutomationFlowRegistry:

    def __init__(self):
        self._flows = {}

    def register(
        self,
        name,
        conditions=None,
        actions=None,
        enabled=True,
    ):

        flow = AutomationFlow(
            name=name,
            conditions=conditions or [],
            actions=actions or [],
            enabled=enabled,
        )

        self._flows[name] = flow

        return flow

    def get(self, name):
        return self._flows.get(name)

    def remove(self, name):
        return self._flows.pop(
            name,
            None,
        )

    def list(self):
        return list(
            self._flows.values()
        )

    def count(self):
        return len(self._flows)

    def clear(self):
        self._flows.clear()


automation_flow_registry = (
    AutomationFlowRegistry()
      )
