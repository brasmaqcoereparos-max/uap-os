from app.modules.automation.action_executor import (
    action_executor,
)


class RuleExecutor:
    def __init__(self):
        self.last_result = None

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
                "reason": "rule_disabled",
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
                allowed = can_execute()
        else:
            conditions_met = getattr(
                rule,
                "conditions_met",
                None,
            )

            if callable(conditions_met):
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

        results = []

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

                results.append({
                    "index": index,
                    "success": (
                        result is not False
                    ),
                    "result": result,
                })

                if (
                    result is False
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
            item["success"]
            for item in results
        )

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


rule_executor = RuleExecutor()
