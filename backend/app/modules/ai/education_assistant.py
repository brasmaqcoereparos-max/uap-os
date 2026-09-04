from app.modules.ai.education_request import (
    AIEducationRequest,
)
from app.modules.ai.education_response import (
    AIEducationResponse,
)


class AIEducationAssistant:

    def explain(
        self,
        request: AIEducationRequest,
    ):
        profile = request.profile

        explanation = (
            f"Explicação sobre "
            f"{request.topic}"
        )

        steps = []

        if profile.step_by_step:
            steps = [
                (
                    "Identificar o objetivo "
                    "do projeto."
                ),
                (
                    "Identificar os "
                    "componentes envolvidos."
                ),
                (
                    "Validar a lógica no "
                    "simulador."
                ),
                (
                    "Somente depois preparar "
                    "a implementação física."
                ),
            ]

        examples = []

        if profile.include_examples:
            examples.append(
                (
                    "Exemplo conceitual "
                    f"relacionado a "
                    f"{request.topic}."
                )
            )

        exercises = []

        if profile.include_exercises:
            exercises.append(
                (
                    "Monte uma proposta "
                    "simulada usando o tema "
                    f"{request.topic}."
                )
            )

        return AIEducationResponse(
            title=request.topic,
            explanation=explanation,
            steps=steps,
            examples=examples,
            exercises=exercises,
        )


ai_education_assistant = (
    AIEducationAssistant()
              )
