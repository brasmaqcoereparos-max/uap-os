from typing import Any


class ConditionEvaluator:

    def evaluate(
        self,
        condition: dict[str, Any],
        analysis: dict[str, Any],
    ) -> bool:

        if not isinstance(condition, dict):
            return False

        if not isinstance(analysis, dict):
            return False

        condition_type = str(
            condition.get(
                "type",
                "",
            )
        ).strip().lower()

        if condition_type == "motion":
            return self._motion(
                condition,
                analysis,
            )

        if condition_type == "person":
            return self._person(
                condition,
                analysis,
            )

        if condition_type == "object":
            return self._object(
                condition,
                analysis,
            )

        if condition_type == "brightness":
            return self._brightness(
                condition,
                analysis,
            )

        if condition_type == "count":
            return self._count(
                condition,
                analysis,
            )

        return False

    def _motion(
        self,
        condition,
        analysis,
    ):

        expected = bool(
            condition.get(
                "value",
                True,
            )
        )

        actual = bool(
            analysis.get(
                "motion",
                {},
            ).get(
                "motion",
                False,
            )
        )

        return actual == expected

    def _person(
        self,
        condition,
        analysis,
    ):

        expected = int(
            condition.get(
                "count",
                1,
            )
        )

        actual = int(
            analysis.get(
                "persons",
                0,
            )
        )

        operator = str(
            condition.get(
                "operator",
                ">=",
            )
        )

        return self._compare(
            actual,
            operator,
            expected,
        )

    def _object(
        self,
        condition,
        analysis,
    ):

        label = condition.get(
            "label"
        )

        detections = analysis.get(
            "detections",
            [],
        )

        if not label:
            return bool(detections)

        return any(
            item.get("class") == label
            for item in detections
            if isinstance(item, dict)
        )

    def _brightness(
        self,
        condition,
        analysis,
    ):

        brightness = float(
            analysis.get(
                "brightness",
                0,
            )
        )

        expected = float(
            condition.get(
                "value",
                0,
            )
        )

        operator = str(
            condition.get(
                "operator",
                ">",
            )
        )

        return self._compare(
            brightness,
            operator,
            expected,
        )

    def _count(
        self,
        condition,
        analysis,
    ):

        actual = len(
            analysis.get(
                "detections",
                [],
            )
        )

        expected = int(
            condition.get(
                "value",
                0,
            )
        )

        operator = str(
            condition.get(
                "operator",
                ">=",
            )
        )

        return self._compare(
            actual,
            operator,
            expected,
        )

    def _compare(
        self,
        actual,
        operator,
        expected,
    ):

        if operator == "==":
            return actual == expected

        if operator == "!=":
            return actual != expected

        if operator == ">":
            return actual > expected

        if operator == ">=":
            return actual >= expected

        if operator == "<":
            return actual < expected

        if operator == "<=":
            return actual <= expected

        return False


condition_evaluator = ConditionEvaluator()
