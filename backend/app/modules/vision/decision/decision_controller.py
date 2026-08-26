from app.modules.vision.decision.decision_service import (
    decision_service,
)


class DecisionController:

    def execute(self, command):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando de decisão inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        if action == "decision.create":

            rule = decision_service.create(
                name=command.get(
                    "name"
                ),
                conditions=command.get(
                    "conditions",
                    [],
                ),
                actions=command.get(
                    "actions",
                    [],
                ),
                enabled=command.get(
                    "enabled",
                    True,
                ),
                mode=command.get(
                    "mode",
                    "all",
                ),
            )

            return rule.to_dict()

        if action == "decision.list":

            return [
                rule.to_dict()
                for rule in decision_service.list()
            ]

        if action == "decision.remove":

            name = command.get(
                "name"
            )

            return bool(
                decision_service.remove(
                    name
                )
            )

        if action == "decision.evaluate":

            return decision_service.evaluate(
                command.get(
                    "analysis",
                    {},
                )
            )

        if action == "decision.actions":

            return decision_service.evaluate_actions(
                command.get(
                    "analysis",
                    {},
                )
            )

        raise ValueError(
            f"Ação de decisão desconhecida: {action}"
        )


decision_controller = DecisionController()
