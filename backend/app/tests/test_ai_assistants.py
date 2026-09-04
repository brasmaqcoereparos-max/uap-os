from app.modules.ai.automation_assistant_service import (
    ai_automation_assistant_service,
)
from app.modules.ai.ui_assistant_service import (
    ai_ui_assistant_service,
)


def test_ai_automation_assistant():
    result = (
        ai_automation_assistant_service
        .propose(
            text=(
                "Criar automação teste"
            ),
            objective="Teste",
        )
    )

    assert "proposal" in result

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_ai_ui_assistant():
    result = (
        ai_ui_assistant_service
        .propose(
            text=(
                "Criar tela inicial"
            ),
            app_type="kiosk",
        )
    )

    assert "proposal" in result

    assert (
        result["target"]
        == "ui"
    )
