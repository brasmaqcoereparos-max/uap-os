from app.modules.vision.decision.decision_registry import (
    decision_registry,
)

from app.modules.vision.decision.decision_engine import (
    decision_engine,
)


class DecisionService:

    def create(
        self,
        name,
        conditions,
        actions,
        enabled=True,
        mode="all",
    ):

        return decision_registry.register(
            name=name,
            conditions=conditions,
            actions=actions,
            enabled=enabled,
            mode=mode,
        )

    def remove(self, name):
        return decision_registry.remove(
            name
        )

    def get(self, name):
        return decision_registry.get(
            name
        )

    def list(self):
        return decision_registry.list()

    def evaluate(self, analysis):

        return decision_engine.evaluate(
            decision_registry.list(),
            analysis,
        )

    def evaluate_actions(
        self,
        analysis,
    ):

        rules = self.evaluate(
            analysis
        )

        actions = []

        for rule in rules:

            for action in rule.actions:

                if action.get(
                    "enabled",
                    True,
                ):
                    actions.append(
                        {
                            "rule": rule.name,
                            "action": action,
                        }
                    )

        return actions


decision_service = DecisionService()
