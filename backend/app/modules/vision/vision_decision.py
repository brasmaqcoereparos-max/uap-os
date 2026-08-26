from typing import Any


class VisionDecision:

    def evaluate(
        self,
        analysis: dict[str, Any],
        rules: list[dict[str, Any]],
    ):

        if not isinstance(
            analysis,
            dict,
        ):
            raise TypeError(
                "Análise Vision inválida."
            )

        if not isinstance(
            rules,
            list,
        ):
            raise TypeError(
                "Regras Vision inválidas."
            )

        decisions = []

        for rule in rules:

            if not isinstance(
                rule,
                dict,
            ):
                continue

            if self._matches(
                analysis,
                rule,
            ):
                decisions.append(
                    {
                        "rule": rule.get(
                            "name",
                            "unnamed",
                        ),
                        "action": rule.get(
                            "action"
                        ),
                        "data": rule.get(
                            "data"
                        ),
                    }
                )

        return decisions

    def _matches(
        self,
        analysis,
        rule,
    ):

        condition = str(
            rule.get(
                "condition",
                "",
            )
        ).strip().lower()

        if condition == "motion":
            return bool(
                analysis.get(
                    "motion",
                    {},
                ).get(
                    "motion",
                    False,
                )
            )

        if condition == "person":
            return (
                int(
                    analysis.get(
                        "persons",
                        0,
                    )
                )
                > 0
            )

        if condition == "object":
            return bool(
                analysis.get(
                    "detections",
                    [],
                )
            )

        return False


vision_decision = VisionDecision()
