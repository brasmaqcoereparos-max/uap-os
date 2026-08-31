"""
Executor de sequências da automação UAP.
"""

from app.modules.automation.action_executor import (
    action_executor,
)


class SequenceExecutor:

    def __init__(self):
        self.running = False

        self.current_step = None

        self.results = []

        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.last_error = None

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
        self.last_error = None

        steps = getattr(
            sequence,
            "steps",
            [],
        )

        try:
            for index, step in enumerate(
                steps
            ):
                if not self.running:
                    break

                self.current_step = index

                if isinstance(
                    step,
                    dict,
                ):
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
                    result = (
                        self._execute_action(
                            action,
                            device=device,
                            context=context,
                        )
                    )

                    success = (
                        result is not False
                    )

                    self.results.append({
                        "index": index,
                        "name": name,
                        "success": success,
                        "result": result,
                    })

                    if (
                        not success
                        and stop_on_error
                    ):
                        break

                except Exception as exc:
                    self.last_error = (
                        str(exc)
                    )

                    self.results.append({
                        "index": index,
                        "name": name,
                        "success": False,
                        "error": str(exc),
                    })

                    if stop_on_error:
                        break

            success = all(
                item["success"]
                for item
                in self.results
            )

            self.execution_count += 1

            if success:
                self.success_count += 1
            else:
                self.failure_count += 1

            result = {
                "success": success,
                "results": list(
                    self.results
                ),
            }

            if hasattr(
                sequence,
                "execution_count",
            ):
                sequence.execution_count += 1

            if hasattr(
                sequence,
                "last_result",
            ):
                sequence.last_result = (
                    result
                )

            return result

        finally:
            self.running = False
            self.current_step = None

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

        return (
            action_executor.execute(
                action,
                device=device,
                context=context,
            )
        )

    def stop(self):
        self.running = False

        return True

    def reset_statistics(self):
        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.results = []
        self.current_step = None

        self.last_error = None

        return True

    def status(self):
        return {
            "running": self.running,
            "current_step": (
                self.current_step
            ),
            "results": list(
                self.results
            ),
            "execution_count": (
                self.execution_count
            ),
            "success_count": (
                self.success_count
            ),
            "failure_count": (
                self.failure_count
            ),
            "last_error": (
                self.last_error
            ),
        }


sequence_executor = (
    SequenceExecutor()
)
