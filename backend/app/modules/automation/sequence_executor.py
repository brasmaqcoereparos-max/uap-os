from app.modules.automation.action_executor import (
    action_executor,
)


class SequenceExecutor:
    def __init__(self):
        self.running = False
        self.current_step = None
        self.results = []

    def execute(
        self,
        sequence,
        device=None,
        context=None,
        stop_on_error=True,
    ):
        if sequence is None:
            raise ValueError(
                "Sequência não informada."
            )

        if not getattr(
            sequence,
            "enabled",
            True,
        ):
            return {
                "success": False,
                "reason": (
                    "sequence_disabled"
                ),
                "results": [],
            }

        self.running = True
        self.current_step = None
        self.results = []

        steps = getattr(
            sequence,
            "steps",
            [],
        )

        for index, step in enumerate(
            steps
        ):
            if not self.running:
                break

            self.current_step = index

            if isinstance(step, dict):
                if not step.get(
                    "enabled",
                    True,
                ):
                    continue

                action = step.get(
                    "action"
                )

                name = step.get(
                    "name",
                    f"step_{index + 1}",
                )

            else:
                action = getattr(
                    step,
                    "action",
                    step,
                )

                name = getattr(
                    step,
                    "name",
                    f"step_{index + 1}",
                )

            try:
                result = self._execute_action(
                    action,
                    device=device,
                    context=context,
                )

                self.results.append({
                    "index": index,
                    "name": name,
                    "success": True,
                    "result": result,
                })

            except Exception as exc:
                self.results.append({
                    "index": index,
                    "name": name,
                    "success": False,
                    "error": str(exc),
                })

                if stop_on_error:
                    self.running = False
                    break

        success = all(
            item["success"]
            for item in self.results
        )

        self.running = False
        self.current_step = None

        return {
            "success": success,
            "results": list(
                self.results
            ),
        }

    @staticmethod
    def _execute_action(
        action,
        device=None,
        context=None,
    ):
        if action is None:
            return None

        if callable(action):
            try:
                return action(
                    context or {}
                )
            except TypeError:
                return action()

        execute = getattr(
            action,
            "execute",
            None,
        )

        if callable(execute):
            try:
                return execute(
                    context or {}
                )
            except TypeError:
                try:
                    return execute(
                        device
                    )
                except TypeError:
                    return execute()

        return action_executor.execute(
            action,
            device=device,
        )

    def stop(self):
        self.running = False

    def status(self):
        return {
            "running": self.running,
            "current_step": (
                self.current_step
            ),
            "results": list(
                self.results
            ),
        }


sequence_executor = SequenceExecutor()
