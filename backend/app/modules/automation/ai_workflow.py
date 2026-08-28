from app.modules.automation.ai_solution import (
    ai_solution_builder,
)


class AIWorkflow:
    STATUS_ERROR = "error"

    STATUS_REVIEW = (
        "ready_for_review"
    )

    STATUS_APPROVED = "approved"

    def __init__(self):
        self.last_solution = None
        self.status = None

    def create(self, request):
        solution = (
            ai_solution_builder.build(
                request
            )
        )

        self.last_solution = solution

        if not solution.get(
            "success",
            False,
        ):
            self.status = (
                self.STATUS_ERROR
            )

            return {
                "status": self.status,
                "solution": solution,
            }

        self.status = (
            self.STATUS_REVIEW
        )

        return {
            "status": self.status,
            "solution": solution,
        }

    def approve(self):
        if (
            self.last_solution
            is None
            or not self.last_solution.get(
                "success",
                False,
            )
        ):
            return False

        self.status = (
            self.STATUS_APPROVED
        )

        return True

    def reject(self):
        if self.last_solution is None:
            return False

        self.status = (
            self.STATUS_ERROR
        )

        return True

    def reset(self):
        self.last_solution = None
        self.status = None

    def get_graph(self):
        if not self.last_solution:
            return None

        return self.last_solution.get(
            "graph"
        )

    def to_dict(self):
        return {
            "status": self.status,
            "has_solution": (
                self.last_solution
                is not None
            ),
            "success": (
                bool(
                    self.last_solution
                    and self.last_solution.get(
                        "success",
                        False,
                    )
                )
            ),
        }


ai_workflow = AIWorkflow()
