from app.modules.ai.provider_manager import (
    ai_provider_manager,
)


def test_ai_provider_manager_initializes():
    providers = (
        ai_provider_manager
        .providers()
    )

    assert isinstance(
        providers,
        list,
    )

    assert len(providers) > 0


def test_ai_has_default_provider():
    provider = (
        ai_provider_manager.get()
    )

    assert provider is not None

    assert hasattr(
        provider,
        "generate",
    )
