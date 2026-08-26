from app.modules.vision.automation.vision_automation_bridge import (
    vision_automation_bridge,
)


class VisionEventActions:

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

            if not isinstance(
                item,
                dict,
            ):
                continue

            action = item.get(
                "action"
            )

            data = item.get(
                "data"
            )

            if not action:
                continue

            results.append(
                vision_automation_bridge.execute(
                    action,
                    data,
                )
            )

        return results


vision_event_actions = (
    VisionEventActions()
          )
