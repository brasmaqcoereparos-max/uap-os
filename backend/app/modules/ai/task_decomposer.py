import uuid

from app.modules.ai.plan import (
    AIPlan,
)
from app.modules.ai.plan_step import (
    AIPlanStep,
)
from app.modules.ai.task import (
    AITask,
)


class AITaskDecomposer:

    def decompose(
        self,
        task: AITask,
    ):
        plan = AIPlan(
            id=str(uuid.uuid4()),
            objective=task.description
            or task.title,
            title=task.title,
        )

        defaults = [
            (
                "understand",
                "Entender objetivo",
                (
                    "Interpretar o objetivo "
                    "e identificar requisitos."
                ),
            ),
            (
                "inspect",
                "Inspecionar contexto",
                (
                    "Verificar recursos, "
                    "módulos e restrições."
                ),
            ),
            (
                "design",
                "Definir solução",
                (
                    "Montar proposta "
                    "estruturada."
                ),
            ),
            (
                "validate",
                "Validar proposta",
                (
                    "Checar compatibilidade, "
                    "segurança e dependências."
                ),
            ),
            (
                "deliver",
                "Entregar resultado",
                (
                    "Gerar saída estruturada "
                    "para o UAP."
                ),
            ),
        ]

        previous = None

        for order, (
            step_id,
            title,
            description,
        ) in enumerate(
            defaults,
            start=1,
        ):
            dependencies = []

            if previous:
                dependencies.append(
                    previous
                )

            step = AIPlanStep(
                id=step_id,
                title=title,
                description=description,
                order=order,
                depends_on=dependencies,
            )

            plan.add_step(step)

            previous = step_id

        return plan


ai_task_decomposer = (
    AITaskDecomposer()
)
