from app.modules.ai.planner_service import (
    ai_planner_service,
)


def test_ai_planner_creates_plan():
    result = (
        ai_planner_service.plan(
            title="Projeto teste",
            description=(
                "Criar automação "
                "de teste"
            ),
        )
    )

    assert "plan" in result
    assert "validation" in result
    assert "proposal" in result


def test_ai_plan_is_valid():
    result = (
        ai_planner_service.plan(
            title="Teste válido",
            description=(
                "Validar projeto"
            ),
        )
    )

    assert (
        result[
            "validation"
        ]["valid"]
        is True
    )
