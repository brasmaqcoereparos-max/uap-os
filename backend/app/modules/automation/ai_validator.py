class AIPlanValidator:

    def validate(self, intent, plan):

        errors = []

        if not intent.goal:
            errors.append(
                "Automation goal not defined"
            )

        if not plan.steps:
            errors.append(
                "Automation plan has no steps"
            )

        return errors

    def is_valid(
        self,
        intent,
        plan,
    ):

        return not self.validate(
            intent,
            plan,
        )


ai_plan_validator = AIPlanValidator()
