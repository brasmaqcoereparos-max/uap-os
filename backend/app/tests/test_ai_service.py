from app.modules.ai.service import (
    ai_service,
)


def test_ai_service_ask():
    response = ai_service.ask(
        text="Teste UAP AI",
        provider_name="mock",
    )

    assert response is not None
    assert response.success is True
    assert response.provider == "mock"


def test_ai_service_lists_providers():
    providers = (
        ai_service.providers()
    )

    assert isinstance(
        providers,
        list,
    )

    assert len(providers) > 0
