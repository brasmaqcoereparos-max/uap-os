from app.modules.automation.graph_validator import (
    graph_validator,
)

from app.modules.automation.graph_runtime import (
    graph_runtime,
)

from app.modules.automation.flow_status import (
    flow_status,
    FlowStatus,
)


class AutomationRuntime:

    def load(self, graph):

        errors = graph_validator.validate(
            graph
        )

        if errors:

            flow_status.set(
                FlowStatus.ERROR,
                "; ".join(errors),
            )

            return False

        graph_runtime.load(graph)

        flow_status.set(
            FlowStatus.READY
        )

        return True

    def start(self):

        if graph_runtime.start():

            flow_status.set(
                FlowStatus.RUNNING
            )

            return True

        return False

    def stop(self):

        graph_runtime.stop()

        flow_status.set(
            FlowStatus.STOPPED
        )


automation_runtime = AutomationRuntime()
