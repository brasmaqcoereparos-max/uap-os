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
    def __init__(self):
        self.graph = None
        self.context = {}

    def load(
        self,
        graph,
        context=None,
    ):
        if graph is None:
            flow_status.set(
                FlowStatus.ERROR,
                "Grafo não informado.",
            )
            return False

        report = graph_validator.report(
            graph
        )

        if not report["valid"]:
            flow_status.set(
                FlowStatus.ERROR,
                "; ".join(
                    report["errors"]
                ),
            )
            return False

        try:
            graph_runtime.load(
                graph,
                context=context,
            )

        except Exception as exc:
            flow_status.set(
                FlowStatus.ERROR,
                str(exc),
            )
            return False

        self.graph = graph
        self.context = dict(
            context or {}
        )

        flow_status.set(
            FlowStatus.READY
        )

        return True

    def start(self):
        if self.graph is None:
            return False

        if graph_runtime.start():
            flow_status.set(
                FlowStatus.RUNNING
            )
            return True

        return False

    def execute_cycle(self):
        if (
            flow_status.get()
            != FlowStatus.RUNNING
        ):
            return None

        try:
            result = (
                graph_runtime.execute_cycle()
            )

            if not graph_runtime.is_active():
                flow_status.set(
                    FlowStatus.COMPLETED
                )

            return result

        except Exception as exc:
            flow_status.set(
                FlowStatus.ERROR,
                str(exc),
                error=exc,
            )
            return None

    def execute_all(
        self,
        max_cycles=10000,
    ):
        if self.graph is None:
            return {
                "success": False,
                "reason": "graph_not_loaded",
            }

        if not graph_runtime.is_active():
            if not self.start():
                return {
                    "success": False,
                    "reason": "start_failed",
                }

        try:
            result = graph_runtime.execute_all(
                max_cycles=max_cycles
            )

            if result.get(
                "success",
                False,
            ):
                flow_status.set(
                    FlowStatus.COMPLETED
                )

            return result

        except Exception as exc:
            flow_status.set(
                FlowStatus.ERROR,
                str(exc),
                error=exc,
            )

            return {
                "success": False,
                "error": str(exc),
            }

    def pause(self):
        if graph_runtime.pause():
            flow_status.set(
                FlowStatus.PAUSED
            )
            return True

        return False

    def resume(self):
        if graph_runtime.resume():
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

        return True

    def reset(self):
        graph_runtime.reset()

        self.graph = None
        self.context = {}

        flow_status.set(
            FlowStatus.CREATED
        )

        return True

    def status(self):
        return {
            "flow": flow_status.to_dict(),
            "runtime": graph_runtime.status(),
        }


automation_runtime = AutomationRuntime()
