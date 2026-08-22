"""
Gerador de explicações das automações criadas pela IA do UAP.
"""


class AIExplanation:

    def explain(
        self,
        intent,
        plan,
    ):

        goal = getattr(
            intent,
            "goal",
            "general",
        )

        steps = list(
            getattr(
                plan,
                "steps",
                [],
            )
        )

        if steps:

            description = (
                "A automação foi organizada "
                "em "
                f"{len(steps)} etapa(s)."
            )

        else:

            description = (
                "A automação ainda não possui "
                "etapas definidas."
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

    def _build_text(
        self,
        goal,
        steps,
    ):

        lines = [
            f"Objetivo identificado: {goal}.",
        ]

        if steps:

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

        else:

            lines.append(
                "Nenhuma etapa foi definida."
            )

        return "\n".join(
            lines
        )


ai_explanation = AIExplanation()
