class AIPlanValidator:
    def validate(
        self,
        intent,
        plan,
    ):
        errors = []

        if intent is None:
            return [
                "Automation intent not defined"
            ]

        if plan is None:
            return [
                "Automation plan not defined"
            ]

        goal = str(
            getattr(
                intent,
                "goal",
                "",
            )
            or ""
        ).strip()

        if not goal:
            errors.append(
                "Automation goal not defined"
            )

        steps = getattr(
            plan,
            "steps",
            None,
        )

        if not isinstance(
            steps,
            list,
        ):
            errors.append(
                "Automation plan steps "
                "must be a list"
            )

            return errors

        if not steps:
            errors.append(
                "Automation plan has no steps"
            )

        for index, step in enumerate(
            steps
        ):
            if isinstance(step, str):
                if not step.strip():
                    errors.append(
                        "Automation plan "
                        f"step {index} is empty"
                    )

                continue

            if not isinstance(
                step,
                dict,
            ):
                errors.append(
                    "Automation plan "
                    f"step {index} is invalid"
                )

                continue

            name = str(
                step.get(
                    "name",
                    step.get(
                        "description",
                        "",
                    ),
                )
                or ""
            ).strip()

            if not name:
                errors.append(
                    "Automation plan "
                    f"step {index} "
                    "has no name"
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

    def report(
        self,
        intent,
        plan,
    ):
        errors = self.validate(
            intent,
            plan,
        )

        return {
            "valid": not errors,
            "errors": errors,
        }


ai_plan_validator = (
    AIPlanValidator()
        )
