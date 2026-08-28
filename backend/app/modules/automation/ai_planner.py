from app.modules.automation.ai_plan import (
    AutomationPlan,
)


class AutomationPlanner:
    TEMPLATES = {
        "stock": [
            "Identificar produto",
            "Obter quantidade atual",
            "Comparar com estoque mínimo",
            "Gerar resultado",
        ],
        "motor": [
            "Verificar condição de início",
            "Preparar acionamento",
            "Executar movimento",
            "Finalizar acionamento",
        ],
        "sensor": [
            "Inicializar sensor",
            "Obter leitura",
            "Validar leitura",
            "Gerar resultado",
        ],
        "measurement": [
            "Obter medida",
            "Validar medida",
            "Registrar resultado",
        ],
        "vision": [
            "Preparar câmera",
            "Capturar imagem",
            "Analisar imagem",
            "Gerar resultado",
        ],
        "robot": [
            "Preparar robô",
            "Validar condições",
            "Executar movimento",
            "Verificar posição",
        ],
        "timer": [
            "Configurar temporizador",
            "Iniciar contagem",
            "Aguardar término",
            "Gerar evento",
        ],
        "output": [
            "Validar saída",
            "Preparar acionamento",
            "Executar saída",
            "Confirmar estado",
        ],
        "general": [
            "Analisar solicitação",
            "Preparar automação",
            "Executar operação",
            "Validar resultado",
        ],
    }

    def create_plan(self, intent):
        if intent is None:
            raise ValueError(
                "Intent não informado."
            )

        goal = str(
            getattr(
                intent,
                "goal",
                "general",
            )
            or "general"
        )

        plan = AutomationPlan(
            goal=goal
        )

        template = (
            self.TEMPLATES.get(
                goal,
                self.TEMPLATES[
                    "general"
                ],
            )
        )

        for index, description in (
            enumerate(
                template,
                start=1,
            )
        ):
            plan.add_step({
                "id": (
                    f"{goal}_{index}"
                ),
                "name": description,
                "description": (
                    description
                ),
                "type": self._step_type(
                    goal,
                    index,
                    len(template),
                ),
                "metadata": {},
            })

        return plan

    @staticmethod
    def _step_type(
        goal,
        index,
        total,
    ):
        if index == 1:
            return "start"

        if index == total:
            return "end"

        if goal in {
            "sensor",
            "measurement",
            "vision",
        }:
            return "input"

        if goal in {
            "motor",
            "robot",
            "output",
        }:
            return "action"

        return "process"


automation_planner = (
    AutomationPlanner()
        )
