"""
Executor de regras da automação UAP.
"""

from app.modules.automation.action_executor import (
    action_executor,
)


class RuleExecutor:

    def __init__(self):
        self.last_result = None

        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.running = False

    def execute(
        self,
        rule,
        device=None,
        context=None,
        stop_on_error=True,
    ):
        if rule is None:
            return False

        if not getattr(
            rule,
            "enabled",
            True,
        ):
            self.last_result = {
                "success": False,
                "reason": (
                    "rule_disabled"
                ),
            }

            return False

        can_execute = getattr(
            rule,
            "can_execute",
            None,
        )

        if callable(can_execute):
            try:
                allowed = can_execute(
                    context
                )

            except TypeError:
                allowed = (
                    can_execute()
                )

        else:
            conditions_met = getattr(
                rule,
                "conditions_met",
                None,
            )

            if callable(
                conditions_met
            ):
                try:
                    allowed = (
                        conditions_met(
                            context
                        )
                    )

                except TypeError:
                    allowed = (
                        conditions_met()
                    )

            else:
                allowed = True

        if not allowed:
            self.last_result = {
                "success": False,
                "reason": (
                    "conditions_not_met"
                ),
            }

            return False

        self.running = True

        results = []

        try:
            for index, action in enumerate(
                getattr(
                    rule,
                    "actions",
                    [],
                )
            ):
                try:
                    result = (
                        action_executor.execute(
                            action,
                            device=device,
                            context=context,
                        )
                    )

                    item_success = (
                        result is not False
                    )

                    results.append({
                        "index": index,
                        "success": (
                            item_success
                        ),
                        "result": result,
                    })

                    if (
                        not item_success
                        and stop_on_error
                    ):
                        break

                except Exception as exc:
                    results.append({
                        "index": index,
                        "success": False,
                        "error": str(exc),
                    })

                    if stop_on_error:
                        break

            success = all(
                item[
                    "success"
                ]
                for item
                in results
            )

            self.execution_count += 1

            if success:
                self.success_count += 1
            else:
                self.failure_count += 1

            if hasattr(
                rule,
                "execution_count",
            ):
                rule.execution_count += 1

            self.last_result = {
                "success": success,
                "rule": getattr(
                    rule,
                    "name",
                    None,
                ),
                "actions": results,
            }

            if hasattr(
                rule,
                "last_result",
            ):
                rule.last_result = (
                    self.last_result
                )

            return success

        finally:
            self.running = False

    def execute_detailed(
        self,
        rule,
        device=None,
        context=None,
    ):
        self.execute(
            rule,
            device=device,
            context=context,
        )

        return self.last_result

    def reset_statistics(self):
        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.last_result = None

        return True

    def status(self):
        return {
            "running": (
                self.running
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
            "last_result": (
                self.last_result
            ),
        }


rule_executor = RuleExecutor()
