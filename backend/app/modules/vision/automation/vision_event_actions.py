from __future__ import annotations

from typing import Any

from app.modules.vision.automation.vision_automation_bridge import (
    vision_automation_bridge,
)


class VisionEventActions:

    def _normalize(
        self,
        item: dict[str, Any],
    ):
        if not isinstance(
            item,
            dict,
        ):
            return None

        rule_name = item.get(
            "rule"
        )

        action_data = item.get(
            "action"
        )

        if isinstance(
            action_data,
            dict,
        ):
            if not action_data.get(
                "enabled",
                True,
            ):
                return None

            action = (
                action_data.get(
                    "action"
                )
                or action_data.get(
                    "name"
                )
            )

            data = (
                action_data.get(
                    "data"
                )
            )

        else:
            action = action_data

            data = item.get(
                "data"
            )

        if not action:
            return None

        return {
            "rule": rule_name,
            "action": str(
                action
            ),
            "data": data,
        }

    def execute_decisions(
        self,
        decisions,
    ):

        if not isinstance(
            decisions,
            list,
        ):
            return []

        results = []

        for item in decisions:

            normalized = (
                self._normalize(
                    item
                )
            )

            if normalized is None:
                continue

            execution = (
                vision_automation_bridge
                .execute(
                    normalized[
                        "action"
                    ],
                    normalized[
                        "data"
                    ],
                )
            )

            results.append(
                {
                    "rule": (
                        normalized[
                            "rule"
                        ]
                    ),
                    "action": (
                        normalized[
                            "action"
                        ]
                    ),
                    "execution": (
                        execution
                    ),
                }
            )

        return results


vision_event_actions = (
    VisionEventActions()
            )
