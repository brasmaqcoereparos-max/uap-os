from __future__ import annotations

import uuid
from datetime import datetime
from datetime import timezone
from typing import Any

from app.modules.metrics.history_service import (
    metrics_history_service,
)


def utc_now():
    return datetime.now(
        timezone.utc
    )


class AlertService:

    VALID_OPERATORS = {
        ">",
        ">=",
        "<",
        "<=",
        "==",
        "!=",
    }

    VALID_LEVELS = {
        "info",
        "warning",
        "critical",
    }

    def __init__(self):

        self._rules: dict[
            str,
            dict[str, Any],
        ] = {}

        self._alerts: dict[
            str,
            dict[str, Any],
        ] = {}

    def register_rule(
        self,
        rule_id: str,
        metric: str,
        operator: str,
        threshold: float,
        *,
        level: str = "warning",
        message: str = "",
        machine_id: str | None = None,
        enabled: bool = True,
    ):

        if (
            operator
            not in self.VALID_OPERATORS
        ):
            raise ValueError(
                "Invalid alert operator"
            )

        normalized_level = str(
            level
        ).strip().lower()

        if (
            normalized_level
            not in self.VALID_LEVELS
        ):
            raise ValueError(
                "Invalid alert level"
            )

        rule = {
            "id": rule_id,
            "metric": metric,
            "operator": operator,
            "threshold": float(
                threshold
            ),
            "level": (
                normalized_level
            ),
            "message": (
                message
                or (
                    f"{metric} {operator} "
                    f"{threshold}"
                )
            ),
            "machine_id": (
                machine_id
            ),
            "enabled": bool(
                enabled
            ),
        }

        self._rules[
            rule_id
        ] = rule

        return dict(
            rule
        )

    def _matches(
        self,
        value: float,
        operator: str,
        threshold: float,
    ):

        if operator == ">":
            return value > threshold

        if operator == ">=":
            return value >= threshold

        if operator == "<":
            return value < threshold

        if operator == "<=":
            return value <= threshold

        if operator == "==":
            return value == threshold

        if operator == "!=":
            return value != threshold

        return False

    def evaluate(
        self,
        metric: str,
        value: float,
        *,
        machine_id: str | None = None,
    ):

        triggered = []

        numeric_value = float(
            value
        )

        for rule in (
            self._rules.values()
        ):

            if not rule[
                "enabled"
            ]:
                continue

            if (
                rule["metric"]
                != metric
            ):
                continue

            rule_machine = (
                rule.get(
                    "machine_id"
                )
            )

            if (
                rule_machine
                is not None
                and rule_machine
                != machine_id
            ):
                continue

            if not self._matches(
                numeric_value,
                rule[
                    "operator"
                ],
                rule[
                    "threshold"
                ],
            ):
                continue

            alert = self._create_alert(
                rule,
                numeric_value,
                machine_id,
            )

            triggered.append(
                alert
            )

        return triggered

    def _create_alert(
        self,
        rule,
        value,
        machine_id,
    ):

        alert_id = str(
            uuid.uuid4()
        )

        alert = {
            "id": alert_id,
            "rule_id": rule[
                "id"
            ],
            "machine_id": (
                machine_id
            ),
            "metric": (
                rule[
                    "metric"
                ]
            ),
            "value": value,
            "threshold": (
                rule[
                    "threshold"
                ]
            ),
            "level": (
                rule[
                    "level"
                ]
            ),
            "message": (
                rule[
                    "message"
                ]
            ),
            "active": True,
            "created_at": (
                utc_now().isoformat()
            ),
            "acknowledged_at": None,
        }

        self._alerts[
            alert_id
        ] = alert

        metrics_history_service.record(
            "alert",
            alert,
            source=machine_id,
        )

        return dict(
            alert
        )

    def acknowledge(
        self,
        alert_id: str,
    ):

        alert = self._alerts.get(
            alert_id
        )

        if alert is None:
            raise KeyError(
                "Alert not found: "
                f"{alert_id}"
            )

        alert[
            "active"
        ] = False

        alert[
            "acknowledged_at"
        ] = (
            utc_now().isoformat()
        )

        metrics_history_service.record(
            "alert_acknowledged",
            alert,
            source=alert.get(
                "machine_id"
            ),
        )

        return dict(
            alert
        )

    def alerts(
        self,
        machine_id: str | None = None,
        *,
        active_only: bool = False,
    ):

        result = list(
            self._alerts.values()
        )

        if machine_id is not None:
            result = [
                alert
                for alert in result
                if alert.get(
                    "machine_id"
                )
                == machine_id
            ]

        if active_only:
            result = [
                alert
                for alert in result
                if alert[
                    "active"
                ]
            ]

        return [
            dict(
                alert
            )
            for alert in result
        ]

    def rules(self):

        return [
            dict(
                rule
            )
            for rule
            in self._rules.values()
        ]

    def clear(self):

        self._rules.clear()
        self._alerts.clear()


alert_service = AlertService()
