from app.modules.automation.action_executor import (
    action_executor,
)


class RuleExecutor:

    def execute(
        self,
        rule,
        device=None,
    ):

        if not rule.conditions_met():
            return False

        for action in rule.actions:

            action_executor.execute(
                action,
                device,
            )

        return True


rule_executor = RuleExecutor()
