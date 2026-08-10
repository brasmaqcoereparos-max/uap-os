from app.modules.automation.ai_plan import (
    AutomationPlan,
)


class AutomationPlanner:

    def create_plan(
        self,
        intent,
    ):

        plan = AutomationPlan()

        if intent.goal == "stock":

            plan.add_step(
                "Identificar produto"
            )

            plan.add_step(
                "Obter quantidade atual"
            )

            plan.add_step(
                "Comparar com estoque mínimo"
            )

            plan.add_step(
                "Gerar alerta"
            )

        elif intent.goal == "motor":

            plan.add_step(
                "Verificar condição"
            )

            plan.add_step(
                "Ligar motor"
            )

            plan.add_step(
                "Executar movimento"
            )

            plan.add_step(
                "Parar motor"
            )

        elif intent.goal == "measurement":

            plan.add_step(
                "Obter medida"
            )

            plan.add_step(
                "Validar medida"
            )

            plan.add_step(
                "Registrar resultado"
            )

        elif intent.goal == "vision":

            plan.add_step(
                "Capturar imagem"
            )

            plan.add_step(
                "Analisar imagem"
            )

            plan.add_step(
                "Gerar resultado"
            )

        elif intent.goal == "robot":

            plan.add_step(
                "Preparar robô"
            )

            plan.add_step(
                "Executar movimento"
            )

            plan.add_step(
                "Verificar posição"
            )

        else:

            plan.add_step(
                "Analisar solicitação"
            )

        return plan


automation_planner = AutomationPlanner()
