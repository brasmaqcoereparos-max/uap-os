from app.modules.vision.automation.automation_flow_registry import (
    automation_flow_registry,
)

from app.modules.vision.decision.condition_evaluator import (
    condition_evaluator,
)

from app.modules.vision.automation.vision_event_actions import (
    vision_event_actions,
)


class AutomationFlowExecutor:

    def execute(
        self,
        flow_name,
        context,
    ):

        flow = automation_flow_registry.get(
            flow_name
        )

        if flow is None:
            raise KeyError(
                f"Fluxo '{flow_name}' não encontrado."
            )

        if not flow.enabled:
            return {
                "success": False,
                "executed": False,
                "reason": "Fluxo desabilitado.",
            }

        conditions = [
            condition_evaluator.evaluate(
                condition,
                context,
            )
            for condition in flow.conditions
        ]

        if conditions and not all(
            conditions
        ):
            return {
                "success": True,
                "executed": False,
                "reason": (
                    "Condições não atendidas."
                ),
            }

        results = (
            vision_event_actions.execute_decisions(
                flow.actions
            )
        )

        return {
            "success": True,
            "executed": True,
            "flow": flow_name,
            "results": results,
        }


automation_flow_executor = (
    AutomationFlowExecutor()
      )
