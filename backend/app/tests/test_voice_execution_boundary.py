import pytest

from app.modules.voice.command import (
    VoiceCommand,
)
from app.modules.voice.confirmation_executor import (
    VoiceConfirmationExecutor,
)
from app.modules.voice.confirmation_manager import (
    VoiceConfirmationManager,
)
from app.modules.voice.dispatch_executor import (
    VoiceDispatchExecutor,
)
from app.modules.voice.policy_defaults import (
    install_default_voice_policies,
)
from app.modules.voice.policy_registry import (
    voice_policy_registry,
)
from app.modules.voice.safe_pipeline import (
    VoiceSafePipeline,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


def test_voice_confirmation_requires_confirmation():
    manager = VoiceConfirmationManager()

    command = VoiceCommand(
        command="application.command",
        parameters={
            "text": "ligar motor",
        },
        requires_confirmation=True,
    )

    confirmation = manager.create(
        command
    )

    assert confirmation.pending() is True
    assert confirmation.confirmed is False
    assert confirmation.cancelled is False


def test_confirmation_cannot_execute_before_confirm():
    from app.modules.voice import (
        confirmation_executor,
    )

    command = VoiceCommand(
        command="application.command",
        parameters={
            "text": "executar comando",
        },
    )

    from app.modules.voice.confirmation_manager import (
        voice_confirmation_manager,
    )

    confirmation = (
        voice_confirmation_manager.create(
            command
        )
    )

    executor = (
        VoiceConfirmationExecutor()
    )

    with pytest.raises(
        ValueError
    ):
        executor.execute(
            confirmation.id
        )

    voice_confirmation_manager.remove(
        confirmation.id
    )


def test_cancelled_confirmation_cannot_execute():
    from app.modules.voice.confirmation_manager import (
        voice_confirmation_manager,
    )

    command = VoiceCommand(
        command="application.command",
        parameters={
            "text": "executar comando",
        },
    )

    confirmation = (
        voice_confirmation_manager.create(
            command
        )
    )

    voice_confirmation_manager.cancel(
        confirmation.id
    )

    executor = (
        VoiceConfirmationExecutor()
    )

    with pytest.raises(
        ValueError
    ):
        executor.execute(
            confirmation.id
        )

    voice_confirmation_manager.remove(
        confirmation.id
    )


def test_safe_pipeline_rejects_empty_transcript():
    pipeline = VoiceSafePipeline()

    transcript = VoiceTranscript(
        text="",
        language="pt-BR",
        confidence=1.0,
        final=True,
    )

    result = pipeline.process_transcript(
        transcript
    )

    assert result[
        "command"
    ] is None

    assert result[
        "dispatch"
    ] is None

    assert result[
        "execution"
    ] is None

    assert result[
        "error"
    ] == "Empty transcript"


def test_navigation_reaches_dispatch_layer():
    voice_policy_registry.clear()

    install_default_voice_policies()

    pipeline = VoiceSafePipeline()

    transcript = VoiceTranscript(
        text="abrir painel",
        language="pt-BR",
        confidence=1.0,
        final=True,
    )

    result = pipeline.process_transcript(
        transcript
    )

    assert result[
        "intent"
    ] is not None

    assert result[
        "command"
    ] is not None

    assert result[
        "command"
    ][
        "command"
    ] == "ui.navigate"

    assert result[
        "dispatch"
    ] is not None


def test_application_command_requires_confirmation():
    voice_policy_registry.clear()

    install_default_voice_policies()

    pipeline = VoiceSafePipeline()

    transcript = VoiceTranscript(
        text="ligar equipamento",
        language="pt-BR",
        confidence=1.0,
        final=True,
    )

    result = pipeline.process_transcript(
        transcript
    )

    assert result[
        "command"
    ][
        "command"
    ] == "application.command"

    assert result[
        "dispatch"
    ][
        "accepted"
    ] is True

    assert result[
        "dispatch"
    ][
        "status"
    ] == "confirmation_required"

    assert result[
        "execution"
    ] is None

    confirmation_id = (
        result[
            "dispatch"
        ][
            "confirmation_id"
        ]
    )

    assert confirmation_id is not None

    from app.modules.voice.confirmation_manager import (
        voice_confirmation_manager,
    )

    voice_confirmation_manager.remove(
        confirmation_id
    )


def test_unknown_voice_command_is_rejected():
    voice_policy_registry.clear()

    install_default_voice_policies()

    dispatcher = (
        VoiceDispatchExecutor()
    )

    command = VoiceCommand(
        command="unsafe.command",
        parameters={},
    )

    result = (
        dispatcher
        .dispatch_and_execute(
            command
        )
    )

    assert result[
        "dispatch"
    ][
        "accepted"
    ] is False

    assert result[
        "execution"
    ] is None


def test_confirmation_manager_confirm_and_cancel():
    manager = VoiceConfirmationManager()

    first = manager.create(
        VoiceCommand(
            command="application.command"
        )
    )

    confirmed = manager.confirm(
        first.id
    )

    assert confirmed is not None
    assert confirmed.confirmed is True
    assert confirmed.pending() is False

    manager.remove(
        first.id
    )

    second = manager.create(
        VoiceCommand(
            command="application.command"
        )
    )

    cancelled = manager.cancel(
        second.id
    )

    assert cancelled is not None
    assert cancelled.cancelled is True
    assert cancelled.pending() is False

    manager.remove(
        second.id
  )
