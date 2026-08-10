from app.modules.automation.ai_solution import (
    ai_solution_builder,
)


class AIWorkflow:

    def create(self, request):

        solution = ai_solution_builder.build(
            request
        )

        if not solution["success"]:

            return solution

        return {
            "status": "ready_for_review",
            "solution": solution,
        }


ai_workflow = AIWorkflow()
