from app.modules.automation.device_registry import (
    device_registry,
)

from app.modules.automation.device_adapter import (
    DeviceAdapter,
)

from app.modules.automation.safe_execution import (
    safe_execution,
)


class AutomationExecutor:

    def execute(
        self,
        device_id,
        action,
        parameters=None,
        approved=False,
    ):

        if not safe_execution.can_execute(
            approved
        ):

            return {
                "success": False,
                "reason": "execution_not_allowed",
            }

        device = device_registry.get(
            device_id
        )

        if device is None:

            return {
                "success": False,
                "reason": "device_not_found",
            }

        adapter = DeviceAdapter(
            device
        )

        result = adapter.execute(
            action,
            parameters,
        )

        return {
            "success": result,
        }


automation_executor = AutomationExecutor()
