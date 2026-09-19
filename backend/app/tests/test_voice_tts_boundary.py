import pytest

from app.modules.voice.callback_tts_provider import (
    VoiceCallbackTTSProvider,
)
from app.modules.voice.multimodal_response import (
    VoiceMultimodalResponse,
)
from app.modules.voice.response import (
    VoiceResponse,
)
from app.modules.voice.tts_manager import (
    VoiceTTSManager,
)
from app.modules.voice.tts_result import (
    VoiceTTSResult,
)


def test_default_text_tts_provider():
    manager = VoiceTTSManager()

    result = manager.synthesize(
        text="Sistema iniciado",
        language="pt-BR",
    )

    assert (
        result.success
        is True
    )

    assert (
        result.provider
        == "text"
    )

    assert (
        result.text
        == "Sistema iniciado"
    )

    assert (
        result.metadata[
            "language"
        ]
        == "pt-BR"
    )


def test_empty_tts_text_is_rejected():
    manager = VoiceTTSManager()

    with pytest.raises(
        ValueError
    ):
        manager.synthesize(
            text=""
        )


def test_callback_tts_provider():
    provider = (
        VoiceCallbackTTSProvider(
            name="test-audio",
            callback=(
                lambda text, language: (
                    VoiceTTSResult(
                        provider="test-audio",
                        text=text,
                        audio=b"audio-data",
                        mime_type=(
                            "audio/wav"
                        ),
                        success=True,
                    )
                )
            ),
        )
    )

    result = provider.synthesize(
        "Comando executado",
        "pt-BR",
    )

    assert (
        result.provider
        == "test-audio"
    )

    assert (
        result.audio
        == b"audio-data"
    )

    assert (
        result.mime_type
        == "audio/wav"
    )

    assert (
        result.metadata[
            "language"
        ]
        == "pt-BR"
    )


def test_manager_registers_real_provider():
    manager = VoiceTTSManager()

    provider = (
        VoiceCallbackTTSProvider(
            name="provider-test",
            callback=(
                lambda text, language: (
                    VoiceTTSResult(
                        provider=(
                            "provider-test"
                        ),
                        text=text,
                        audio=b"123",
                        mime_type=(
                            "audio/mpeg"
                        ),
                    )
                )
            ),
        )
    )

    manager.register(
        provider
    )

    result = manager.synthesize(
        text="Teste",
        provider_name=(
            "provider-test"
        ),
    )

    assert (
        result.provider
        == "provider-test"
    )

    assert (
        result.audio
        == b"123"
    )


def test_unavailable_tts_provider_is_blocked():
    manager = VoiceTTSManager()

    provider = (
        VoiceCallbackTTSProvider(
            name="offline-tts",
            callback=(
                lambda text, language: (
                    VoiceTTSResult(
                        provider="offline-tts",
                        text=text,
                    )
                )
            ),
            available_callback=(
                lambda: False
            ),
        )
    )

    manager.register(
        provider
    )

    with pytest.raises(
        RuntimeError
    ):
        manager.synthesize(
            text="Teste",
            provider_name=(
                "offline-tts"
            ),
        )


def test_provider_must_return_tts_result():
    provider = (
        VoiceCallbackTTSProvider(
            name="invalid-provider",
            callback=(
                lambda text, language: (
                    "invalid"
                )
            ),
        )
    )

    with pytest.raises(
        TypeError
    ):
        provider.synthesize(
            "Teste"
        )


def test_manager_provider_listing():
    manager = VoiceTTSManager()

    providers = (
        manager.providers()
    )

    text_provider = next(
        provider
        for provider
        in providers
        if provider["name"]
        == "text"
    )

    assert (
        text_provider[
            "available"
        ]
        is True
    )

    assert (
        "default"
        in text_provider
    )


def test_multimodal_response_uses_tts():
    response = VoiceResponse(
        text="Operação concluída",
        speak=True,
        display=True,
        level="success",
    )

    multimodal = (
        VoiceMultimodalResponse()
    )

    result = multimodal.build(
        response,
        language="pt-BR",
    )

    assert (
        result[
            "response"
        ][
            "text"
        ]
        == "Operação concluída"
    )

    assert (
        result[
            "tts"
        ]
        is not None
    )

    assert (
        result[
            "tts"
        ][
            "success"
        ]
        is True
    )

    assert (
        result[
            "feedback"
        ][
            "feedback_type"
        ]
        == "success"
    )


def test_multimodal_response_can_disable_speech():
    response = VoiceResponse(
        text="Mensagem visual",
        speak=False,
        display=True,
    )

    multimodal = (
        VoiceMultimodalResponse()
    )

    result = multimodal.build(
        response
    )

    assert (
        result["tts"]
        is None
  )
