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
        context=None,
    ):
        if not safe_execution.can_execute(
            approved
        ):
            return {
                "success": False,
                "reason": "execution_not_allowed",
                "device_id": str(device_id),
                "action": str(action),
            }

        device = device_registry.get(
            str(device_id)
        )

        if device is None:
            return {
                "success": False,
                "reason": "device_not_found",
                "device_id": str(device_id),
                "action": str(action),
            }

        adapter = DeviceAdapter(device)

        try:
            result = adapter.execute(
                action=action,
                parameters=parameters,
                context=context,
            )

            return {
                "success": result is not False,
                "device_id": str(device_id),
                "action": str(action),
                "result": result,
            }

        except Exception as exc:
            return {
                "success": False,
                "reason": "execution_error",
                "device_id": str(device_id),
                "action": str(action),
                "error": str(exc),
            }

    def read(
        self,
        device_id,
        attribute,
        default=None,
    ):
        device = device_registry.get(
            str(device_id)
        )

        if device is None:
            return default

        adapter = DeviceAdapter(device)

        return adapter.read(
            attribute,
            default,
        )


automation_executor = AutomationExecutor()
