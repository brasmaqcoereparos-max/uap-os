from app.modules.automation.graph_validator import (
    graph_validator,
)


class GraphExecutor:

    def __init__(self):
        self.running = False
        self.last_result = None

    def start(self):
        self.running = True
        return True

    def stop(self):
        self.running = False
        return True

    def reset(self):
        self.running = False
        self.last_result = None

    def _execute_block(
        self,
        block_id,
        block,
        context,
    ):
        if not getattr(
            block,
            "enabled",
            True,
        ):
            return {
                "block_id": block_id,
                "executed": False,
                "reason": "disabled",
            }

        executor = getattr(
            block,
            "execute",
            None,
        )

        if callable(executor):
            try:
                result = executor(
                    context
                )
            except TypeError:
                result = executor()

            return {
                "block_id": block_id,
                "executed": True,
                "result": result,
            }

        runner = getattr(
            block,
            "run",
            None,
        )

        if callable(runner):
            try:
                result = runner(
                    context
                )
            except TypeError:
                result = runner()

            return {
                "block_id": block_id,
                "executed": True,
                "result": result,
            }

        return {
            "block_id": block_id,
            "executed": True,
            "result": None,
        }

    def execute(
        self,
        graph,
        context=None,
        auto_start=True,
    ):
        validation = (
            graph_validator.report(
                graph
            )
        )

        if not validation["valid"]:
            self.last_result = {
                "success": False,
                "validation": validation,
                "executed": [],
            }

            return self.last_result

        if auto_start:
            self.start()

        if not self.running:
            self.last_result = {
                "success": False,
                "error": (
                    "Graph executor is stopped"
                ),
                "executed": [],
            }

            return self.last_result

        context = dict(
            context or {}
        )

        order_method = getattr(
            graph,
            "topological_order",
            None,
        )

        if callable(order_method):
            order = order_method()
        else:
            order = list(
                graph.blocks.keys()
            )

        executed = []

        for block_id in order:
            if not self.running:
                break

            block = graph.blocks.get(
                block_id
            )

            if block is None:
                continue

            result = self._execute_block(
                block_id,
                block,
                context,
            )

            executed.append(
                result
            )

            context["last_block"] = (
                block_id
            )

            context[
                "last_result"
            ] = result.get(
                "result"
            )

            context.setdefault(
                "results",
                {},
            )[block_id] = result.get(
                "result"
            )

        self.last_result = {
            "success": True,
            "validation": validation,
            "executed": executed,
            "context": context,
        }

        return self.last_result

    def status(self):
        return {
            "running": self.running,
            "last_result": (
                self.last_result
            ),
        }


graph_executor = GraphExecutor()
