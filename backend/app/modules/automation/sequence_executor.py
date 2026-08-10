from app.modules.automation.action_executor import (
    action_executor,
)


class SequenceExecutor:

    def execute(
        self,
        sequence,
        device=None,
    ):

        for step in sequence.steps:

            if hasattr(
                step,
                "action",
            ):

                action_executor.execute(
                    step.action,
                    device,
                )


sequence_executor = SequenceExecutor()
