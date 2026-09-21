from __future__ import annotations

from app.modules.ai.education_request import (
    AIEducationRequest,
)
from app.modules.ai.education_response import (
    AIEducationResponse,
)


class AIEducationAssistant:

    VALID_LEVELS = {
        "beginner",
        "intermediate",
        "professional",
    }

    def explain(
        self,
        request: AIEducationRequest,
    ):
        if not isinstance(
            request,
            AIEducationRequest,
        ):
            raise TypeError(
                "request must be an "
                "AIEducationRequest"
            )

        profile = request.profile

        level = str(
            profile.level
        ).strip().lower()

        if level not in self.VALID_LEVELS:
            raise ValueError(
                "Unsupported education level: "
                f"{profile.level}"
            )

        topic = str(
            request.topic
        ).strip()

        if not topic:
            raise ValueError(
                "Education topic "
                "cannot be empty"
            )

        question = str(
            request.question
            or ""
        ).strip()

        explanation = (
            self._explanation(
                topic=topic,
                question=question,
                level=level,
            )
        )

        steps = []

        if profile.step_by_step:
            steps = self._steps(
                topic=topic,
                level=level,
            )

        examples = []

        if profile.include_examples:
            examples = self._examples(
                topic=topic,
                level=level,
            )

        exercises = []

        if profile.include_exercises:
            exercises = (
                self._exercises(
                    topic=topic,
                    level=level,
                )
            )

        warnings = [
            (
                "Use simulation before "
                "physical deployment."
            ),
            (
                "Hardware actions must pass "
                "through Runtime/Safety."
            ),
        ]

        return AIEducationResponse(
            title=topic,
            explanation=explanation,
            steps=steps,
            examples=examples,
            exercises=exercises,
            warnings=warnings,
        )

    def _explanation(
        self,
        *,
        topic: str,
        question: str,
        level: str,
    ) -> str:

        if level == "beginner":
            base = (
                f"{topic} será explicado "
                "de forma visual e simples, "
                "sem exigir programação textual."
            )

        elif level == "intermediate":
            base = (
                f"{topic} será explicado usando "
                "blocos, eventos, condições, "
                "entradas e saídas."
            )

        else:
            base = (
                f"{topic} será explicado com "
                "detalhes técnicos, fluxo, "
                "interfaces, parâmetros e "
                "contratos do sistema."
            )

        if question:
            base += (
                " Pergunta atual: "
                f"{question}"
            )

        return base

    def _steps(
        self,
        *,
        topic: str,
        level: str,
    ):
        steps = [
            "Definir o objetivo.",
            (
                "Identificar os componentes "
                "envolvidos."
            ),
            (
                "Montar a lógica visual."
            ),
            (
                "Executar a lógica no "
                "simulador."
            ),
            (
                "Verificar o resultado."
            ),
        ]

        if level in {
            "intermediate",
            "professional",
        }:
            steps.append(
                (
                    "Analisar condições, "
                    "eventos e estados."
                )
            )

        if level == "professional":
            steps.extend(
                [
                    (
                        "Validar contratos "
                        "entre módulos."
                    ),
                    (
                        "Analisar target, "
                        "hardware e deploy."
                    ),
                ]
            )

        return steps

    def _examples(
        self,
        *,
        topic: str,
        level: str,
    ):
        examples = [
            (
                "Exemplo simulado relacionado "
                f"a {topic}."
            )
        ]

        if level != "beginner":
            examples.append(
                (
                    "Exemplo com entrada, "
                    "condição e saída."
                )
            )

        return examples

    def _exercises(
        self,
        *,
        topic: str,
        level: str,
    ):
        if level == "beginner":
            return [
                (
                    "Monte no simulador uma "
                    f"sequência simples sobre "
                    f"{topic}."
                )
            ]

        if level == "intermediate":
            return [
                (
                    "Crie no simulador um fluxo "
                    f"de {topic} usando uma "
                    "condição."
                )
            ]

        return [
            (
                "Projete, simule e valide um "
                f"fluxo completo de {topic}, "
                "incluindo entradas, saídas "
                "e tratamento de falhas."
            )
        ]


ai_education_assistant = (
    AIEducationAssistant()
        )
