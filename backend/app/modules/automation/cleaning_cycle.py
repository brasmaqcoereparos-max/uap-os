class CleaningCycle:

    def __init__(
        self,
        decision_engine,
        executor,
    ):

        self.decision_engine = decision_engine
        self.executor = executor

        self.active = False

    def start(self):

        self.active = True

    def stop(self):

        self.active = False

    def update(
        self,
        distance=None,
    ):

        if not self.active:

            return None

        decision = self.decision_engine.evaluate(
            distance
        )

        if decision.decision == "continue":

            return decision

        if decision.decision == "stop":

            self.executor.execute(
                self._stop_action()
            )

        elif decision.decision == "return_base":

            self.executor.execute(
                self._return_action()
            )

        return decision

    def _stop_action(self):

        from app.modules.automation.cleaning_action import (
            CleaningAction,
        )

        return CleaningAction(
            CleaningAction.STOP
        )

    def _return_action(self):

        from app.modules.automation.cleaning_action import (
            CleaningAction,
        )

        return CleaningAction(
            CleaningAction.RETURN_BASE
        )
