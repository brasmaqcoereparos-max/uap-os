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
from app.modules.voice.recognizer_manager import (
    voice_recognizer_manager,
)
from app.modules.voice.safe_pipeline import (
    VoiceSafePipeline,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


def test_text_pipeline_builds_response():
    pipeline = VoiceSafePipeline()

    transcript = VoiceTranscript(
        text="abrir painel",
        language="pt-BR",
        confidence=1.0,
        final=True,
    )

    result = (
        pipeline.process_transcript(
            transcript
        )
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
        result["feedback"]
        is not None
    )


def test_command_confirmation_generates_voice_response():
    pipeline = VoiceSafePipeline()

    transcript = VoiceTranscript(
        text="ligar equipamento",
        language="pt-BR",
        confidence=1.0,
        final=True,
    )

    result = (
        pipeline.process_transcript(
            transcript
        )
    )

    assert (
        result[
            "dispatch"
        ][
            "status"
        ]
        == "confirmation_required"
    )

    assert (
        result[
            "execution"
        ]
        is None
    )

    assert (
        result[
            "response"
        ][
            "level"
        ]
        == "warning"
    )

    assert (
        result[
            "response"
        ][
            "metadata"
        ][
            "confirmation_id"
        ]
        is not None
    )

    assert (
        result["tts"]
        is not None
    )


def test_empty_transcript_generates_error_response():
    pipeline = VoiceSafePipeline()

    result = (
        pipeline.process_transcript(
            VoiceTranscript(
                text="",
                language="pt-BR",
                final=True,
            )
        )
    )

    assert (
        result["error"]
        == "Empty transcript"
    )

    assert (
        result[
            "response"
        ][
            "level"
        ]
        == "error"
    )


def test_pipeline_can_disable_response_generation():
    pipeline = VoiceSafePipeline()

    result = (
        pipeline.process_transcript(
            VoiceTranscript(
                text="abrir painel",
                language="pt-BR",
                final=True,
            ),
            build_response=False,
        )
    )

    assert (
        "response"
        not in result
    )

    assert (
        "tts"
        not in result
    )


def test_audio_pipeline_reaches_safe_pipeline():
    recognizer = (
        VoiceCallbackRecognizer(
            name="full-pipeline-stt",
            callback=(
                lambda audio, language: (
                    VoiceTranscript(
                        text="abrir painel",
                        language=language,
                        confidence=1.0,
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
        "complete-pipeline"
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

    pipeline = VoiceAudioPipeline()

    result = pipeline.process(
        stream=stream,
        language="pt-BR",
        recognizer_name=(
            "full-pipeline-stt"
        ),
    )

    assert (
        result["transcript"][
            "text"
        ]
        == "abrir painel"
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

    assert (
        result["audio"][
            "stream_id"
        ]
        == "complete-pipeline"
    )


def test_audio_command_still_requires_confirmation():
    recognizer = (
        VoiceCallbackRecognizer(
            name="safe-command-stt",
            callback=(
                lambda audio, language: (
                    VoiceTranscript(
                        text="ligar motor",
                        language=language,
                        confidence=1.0,
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
        "safe-command"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"audio",
            sequence=0,
            final=True,
        )
    )

    result = (
        VoiceAudioPipeline()
        .process(
            stream=stream,
            recognizer_name=(
                "safe-command-stt"
            ),
        )
    )

    assert (
        result[
            "dispatch"
        ][
            "status"
        ]
        == "confirmation_required"
    )

    assert (
        result["execution"]
        is None
  )
