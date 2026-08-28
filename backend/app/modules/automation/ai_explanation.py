class AIExplanation:
    @staticmethod
    def _step_text(step):
        if isinstance(step, dict):
            return str(
                step.get(
                    "description",
                    step.get(
                        "name",
                        "",
                    ),
                )
            )

        return str(step)

    def explain(
        self,
        intent,
        plan,
    ):
        goal = str(
            getattr(
                intent,
                "goal",
                "general",
            )
            or "general"
        )

        steps = [
            self._step_text(step)
            for step in list(
                getattr(
                    plan,
                    "steps",
                    [],
                )
            )
        ]

        if steps:
            description = (
                "A automação foi "
                f"organizada em "
                f"{len(steps)} etapa(s)."
            )
        else:
            description = (
                "A automação ainda "
                "não possui etapas "
                "definidas."
            )

        return {
            "goal": goal,
            "description": description,
            "steps": steps,
            "text": self._build_text(
                goal,
                steps,
            ),
        }

    @staticmethod
    def _build_text(
        goal,
        steps,
    ):
        lines = [
            (
                "Objetivo identificado: "
                f"{goal}."
            )
        ]

        if not steps:
            lines.append(
                "Nenhuma etapa "
                "foi definida."
            )

            return "\n".join(lines)

        lines.append(
            "Sequência de execução:"
        )

        for index, step in enumerate(
            steps,
            start=1,
        ):
            lines.append(
                f"{index}. {step}"
            )

        return "\n".join(lines)


ai_explanation = AIExplanation()
