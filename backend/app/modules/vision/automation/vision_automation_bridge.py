from app.modules.vision.automation.vision_action_executor import (
    vision_action_executor,
)


class VisionAutomationBridge:

    def register_action(
        self,
        action,
        handler,
    ):
        return vision_action_executor.register(
            action,
            handler,
        )

    def unregister_action(
        self,
        action,
    ):
        return vision_action_executor.unregister(
            action
        )

    def execute(
        self,
        action,
        data=None,
    ):
        return vision_action_executor.execute(
            action,
            data,
        )

    def available_actions(self):
        return vision_action_executor.list()


vision_automation_bridge = (
    VisionAutomationBridge()
)
