from app.modules.automation.cleaning_decision import (
    CleaningDecision,
)


class CleaningDecisionEngine:

    def __init__(
        self,
        safety,
        battery,
    ):

        self.safety = safety
        self.battery = battery

    def evaluate(
        self,
        distance=None,
    ):

        decision = CleaningDecision()

        if not self.safety.allow_movement(
            distance
        ):

            decision.set(
                CleaningDecision.STOP,
                "safety",
            )

            return decision

        if self.battery.is_critical():

            decision.set(
                CleaningDecision.RETURN_BASE,
                "critical_battery",
            )

            return decision

        if self.battery.is_low():

            decision.set(
                CleaningDecision.RETURN_BASE,
                "low_battery",
            )

            return decision

        decision.set(
            CleaningDecision.CONTINUE,
            "normal",
        )

        return decision
