import pytest

from app.modules.voice.audio_chunk import (
    VoiceAudioChunk,
)
from app.modules.voice.audio_pipeline import (
    VoiceAudioPipeline,
)
from app.modules.voice.audio_stream import (
    VoiceAudioStream,
)
from app.modules.voice.callback_recognizer import (
    VoiceCallbackRecognizer,
)
from app.modules.voice.callback_tts_provider import (
    VoiceCallbackTTSProvider,
)
from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.confirmation_executor import (
    voice_confirmation_executor,
)
from app.modules.voice.confirmation_manager import (
    voice_confirmation_manager,
)
from app.modules.voice.policy_defaults import (
    install_default_voice_policies,
)
from app.modules.voice.policy_registry import (
    voice_policy_registry,
)
from app.modules.voice.recognizer_manager import (
    voice_recognizer_manager,
)
from app.modules.voice.safe_pipeline import (
    VoiceSafePipeline,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)
from app.modules.voice.tts_manager import (
    voice_tts_manager,
)
from app.modules.voice.tts_result import (
    VoiceTTSResult,
)


def reset_voice_policies():
    voice_policy_registry.clear()

    install_default_voice_policies()


def test_block9_text_to_intent_command_boundary():
    reset_voice_policies()

    pipeline = VoiceSafePipeline()

    transcript = VoiceTranscript(
        text="ligar motor",
        language="pt-BR",
        confidence=0.99,
        final=True,
    )

    result = (
        pipeline.process_transcript(
            transcript
        )
    )

    assert (
        result["transcript"]["text"]
        == "ligar motor"
    )

    assert (
        result["intent"]["name"]
        == "command"
    )

    assert (
        result["command"]["command"]
        == "application.command"
    )

    assert (
        result["command"][
            "requires_confirmation"
        ]
        is True
    )


def test_block9_dangerous_application_command_requires_confirmation():
    reset_voice_policies()

    pipeline = VoiceSafePipeline()

    result = (
        pipeline.process_transcript(
            VoiceTranscript(
                text="ligar equipamento",
                language="pt-BR",
                confidence=1.0,
                final=True,
            )
        )
    )

    dispatch = result[
        "dispatch"
    ]

    assert (
        dispatch["accepted"]
        is True
    )

    assert (
        dispatch["status"]
        == "confirmation_required"
    )

    assert (
        dispatch["confirmation_id"]
        is not None
    )

    assert (
        result["execution"]
        is None
    )

    confirmation_id = (
        dispatch[
            "confirmation_id"
        ]
    )

    voice_confirmation_manager.remove(
        confirmation_id
    )


def test_block9_confirmation_executes_only_after_confirmation():
    command = VoiceCommand(
        command="application.command",
        parameters={
            "text": "comando confirmado",
        },
        requires_confirmation=True,
    )

    confirmation = (
        voice_confirmation_manager
        .create(
            command
        )
    )

    with pytest.raises(
        ValueError
    ):
        voice_confirmation_executor.execute(
            confirmation.id
        )

    voice_confirmation_manager.confirm(
        confirmation.id
    )

    execution = (
        voice_confirmation_executor
        .execute(
            confirmation.id
        )
    )

    assert (
        execution.executed
        is True
    )

    assert (
        execution.status
        == "executed"
    )

    assert (
        voice_confirmation_manager
        .get(
            confirmation.id
        )
        is None
    )


def test_block9_cancelled_command_never_executes():
    command = VoiceCommand(
        command="application.command",
        parameters={
            "text": "comando cancelado",
        },
        requires_confirmation=True,
    )

    confirmation = (
        voice_confirmation_manager
        .create(
            command
        )
    )

    voice_confirmation_manager.cancel(
        confirmation.id
    )

    with pytest.raises(
        ValueError
    ):
        voice_confirmation_executor.execute(
            confirmation.id
        )

    voice_confirmation_manager.remove(
        confirmation.id
    )


def test_block9_audio_to_stt_boundary():
    recognizer_name = (
        "block9-final-stt"
    )

    recognizer = (
        VoiceCallbackRecognizer(
            name=recognizer_name,
            callback=(
                lambda audio, language: (
                    VoiceTranscript(
                        text="ligar motor",
                        language=language,
                        confidence=0.98,
                        final=True,
                    )
                )
            ),
        )
    )

    voice_recognizer_manager.register(
        recognizer
    )

    stream = VoiceAudioStream(
        "block9-final-audio"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"audio-part-1",
            sequence=0,
            sample_rate=16000,
            channels=1,
            sample_width=2,
        )
    )

    stream.write(
        VoiceAudioChunk(
            data=b"audio-part-2",
            sequence=1,
            final=True,
            sample_rate=16000,
            channels=1,
            sample_width=2,
        )
    )

    transcript = (
        voice_recognizer_manager
        .recognize(
            audio=stream.buffer,
            language="pt-BR",
            recognizer_name=(
                recognizer_name
            ),
        )
    )

    assert (
        transcript.text
        == "ligar motor"
    )

    assert (
        transcript.language
        == "pt-BR"
    )

    assert (
        transcript.metadata[
            "recognizer"
        ]
        == recognizer_name
    )

    assert (
        stream.buffer.data()
        == (
            b"audio-part-1"
            b"audio-part-2"
        )
    )

    assert stream.closed is True


def test_block9_complete_audio_pipeline_boundary():
    reset_voice_policies()

    recognizer_name = (
        "block9-complete-stt"
    )

    recognizer = (
        VoiceCallbackRecognizer(
            name=recognizer_name,
            callback=(
                lambda audio, language: (
                    VoiceTranscript(
                        text=(
                            "ligar equipamento"
                        ),
                        language=language,
                        confidence=0.99,
                        final=True,
                    )
                )
            ),
        )
    )

    voice_recognizer_manager.register(
        recognizer
    )

    stream = VoiceAudioStream(
        "block9-complete"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"voice-data",
            sequence=0,
            final=True,
            sample_rate=16000,
            channels=1,
            sample_width=2,
        )
    )

    result = (
        VoiceAudioPipeline()
        .process(
            stream=stream,
            language="pt-BR",
            recognizer_name=(
                recognizer_name
            ),
        )
    )

    assert (
        result["transcript"]["text"]
        == "ligar equipamento"
    )

    assert (
        result["intent"]["name"]
        == "command"
    )

    assert (
        result["command"]["command"]
        == "application.command"
    )

    assert (
        result["dispatch"]["status"]
        == "confirmation_required"
    )

    assert (
        result["execution"]
        is None
    )

    assert (
        result["response"]
        is not None
    )

    assert (
        result["tts"]
        is not None
    )

    assert (
        result["feedback"]
        is not None
    )

    assert (
        result["audio"]["stream_id"]
        == "block9-complete"
    )

    confirmation_id = (
        result["dispatch"][
            "confirmation_id"
        ]
    )

    if confirmation_id:
        voice_confirmation_manager.remove(
            confirmation_id
        )


def test_block9_tts_provider_boundary():
    provider_name = (
        "block9-final-tts"
    )

    provider = (
        VoiceCallbackTTSProvider(
            name=provider_name,
            callback=(
                lambda text, language: (
                    VoiceTTSResult(
                        provider=(
                            provider_name
                        ),
                        text=text,
                        audio=b"tts-audio",
                        mime_type=(
                            "audio/wav"
                        ),
                        success=True,
                    )
                )
            ),
        )
    )

    voice_tts_manager.register(
        provider
    )

    result = (
        voice_tts_manager
        .synthesize(
            text=(
                "Comando aguardando "
                "confirmação"
            ),
            language="pt-BR",
            provider_name=(
                provider_name
            ),
        )
    )

    assert (
        result.success
        is True
    )

    assert (
        result.provider
        == provider_name
    )

    assert (
        result.audio
        == b"tts-audio"
    )

    assert (
        result.mime_type
        == "audio/wav"
    )


def test_block9_empty_voice_input_fails_safely():
    reset_voice_policies()

    pipeline = VoiceSafePipeline()

    result = (
        pipeline.process_transcript(
            VoiceTranscript(
                text="",
                language="pt-BR",
                confidence=1.0,
                final=True,
            )
        )
    )

    assert (
        result["command"]
        is None
    )

    assert (
        result["dispatch"]
        is None
    )

    assert (
        result["execution"]
        is None
    )

    assert (
        result["error"]
        == "Empty transcript"
    )

    assert (
        result["response"]["level"]
        == "error"
    )


def test_block9_unknown_command_cannot_bypass_policy():
    reset_voice_policies()

    from app.modules.voice.dispatch_executor import (
        VoiceDispatchExecutor,
    )

    dispatcher = (
        VoiceDispatchExecutor()
    )

    result = (
        dispatcher
        .dispatch_and_execute(
            VoiceCommand(
                command=(
                    "hardware.direct_write"
                ),
                parameters={
                    "pin": "GPIO18",
                    "value": True,
                },
            )
        )
    )

    assert (
        result["dispatch"][
            "accepted"
        ]
        is False
    )

    assert (
        result["execution"]
        is None
    )


def test_block9_pipeline_contract_complete():
    reset_voice_policies()

    pipeline = VoiceSafePipeline()

    result = (
        pipeline.process_transcript(
            VoiceTranscript(
                text="ligar motor",
                language="pt-BR",
                confidence=1.0,
                final=True,
            )
        )
    )

    required_layers = {
        "transcript",
        "intent",
        "command",
        "dispatch",
        "execution",
        "response",
        "tts",
        "feedback",
    }

    assert (
        required_layers
        .issubset(
            result.keys()
        )
    )

    assert (
        result["transcript"]
        is not None
    )

    assert (
        result["intent"]
        is not None
    )

    assert (
        result["command"]
        is not None
    )

    assert (
        result["dispatch"]
        is not None
    )

    assert (
        result["response"]
        is not None
    )

    assert (
        result["tts"]
        is not None
    )

    confirmation_id = (
        result["dispatch"].get(
            "confirmation_id"
        )
    )

    if confirmation_id:
        voice_confirmation_manager.remove(
            confirmation_id
)
