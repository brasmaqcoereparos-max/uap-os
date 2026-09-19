import pytest

from app.modules.voice.audio_chunk import (
    VoiceAudioChunk,
)
from app.modules.voice.audio_stream import (
    VoiceAudioStream,
)
from app.modules.voice.callback_recognizer import (
    VoiceCallbackRecognizer,
)
from app.modules.voice.recognizer_manager import (
    VoiceRecognizerManager,
)
from app.modules.voice.transcript import (
    VoiceTranscript,
)


def test_audio_stream_accepts_consistent_chunks():
    stream = VoiceAudioStream(
        "stream-1"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"abc",
            sequence=0,
            sample_rate=16000,
            channels=1,
            sample_width=2,
        )
    )

    stream.write(
        VoiceAudioChunk(
            data=b"def",
            sequence=1,
            final=True,
            sample_rate=16000,
            channels=1,
            sample_width=2,
        )
    )

    assert stream.closed is True

    assert (
        stream.buffer.data()
        == b"abcdef"
    )

    assert (
        stream.audio_format()
        == {
            "sample_rate": 16000,
            "channels": 1,
            "sample_width": 2,
        }
    )


def test_audio_stream_rejects_duplicate_sequence():
    stream = VoiceAudioStream(
        "stream-2"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"a",
            sequence=0,
        )
    )

    with pytest.raises(
        ValueError
    ):
        stream.write(
            VoiceAudioChunk(
                data=b"b",
                sequence=0,
            )
        )


def test_audio_stream_rejects_format_change():
    stream = VoiceAudioStream(
        "stream-3"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"a",
            sequence=0,
            sample_rate=16000,
        )
    )

    with pytest.raises(
        ValueError
    ):
        stream.write(
            VoiceAudioChunk(
                data=b"b",
                sequence=1,
                sample_rate=44100,
            )
        )


def test_callback_recognizer_contract():
    stream = VoiceAudioStream(
        "stream-4"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"audio",
            sequence=0,
            final=True,
        )
    )

    recognizer = (
        VoiceCallbackRecognizer(
            name="test-stt",
            callback=lambda audio, language: (
                VoiceTranscript(
                    text="ligar máquina",
                    language=language,
                    confidence=0.95,
                    final=True,
                )
            ),
        )
    )

    result = recognizer.recognize(
        stream.buffer,
        "pt-BR",
    )

    assert (
        result.text
        == "ligar máquina"
    )

    assert (
        result.language
        == "pt-BR"
    )

    assert (
        result.metadata[
            "recognizer"
        ]
        == "test-stt"
    )


def test_recognizer_manager_accepts_provider():
    manager = VoiceRecognizerManager()

    stream = VoiceAudioStream(
        "stream-5"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"audio",
            sequence=0,
            final=True,
        )
    )

    recognizer = (
        VoiceCallbackRecognizer(
            name="provider-test",
            callback=lambda audio, language: (
                VoiceTranscript(
                    text="abrir painel",
                    language=language,
                    confidence=0.9,
                )
            ),
        )
    )

    manager.register(
        recognizer
    )

    transcript = manager.recognize(
        audio=stream.buffer,
        language="pt-BR",
        recognizer_name=(
            "provider-test"
        ),
    )

    assert (
        transcript.text
        == "abrir painel"
    )

    assert (
        transcript.metadata[
            "recognizer"
        ]
        == "provider-test"
    )


def test_unavailable_recognizer_is_blocked():
    manager = VoiceRecognizerManager()

    stream = VoiceAudioStream(
        "stream-6"
    )

    stream.write(
        VoiceAudioChunk(
            data=b"audio",
            sequence=0,
            final=True,
        )
    )

    recognizer = (
        VoiceCallbackRecognizer(
            name="offline-provider",
            callback=lambda audio, language: (
                VoiceTranscript(
                    text="test"
                )
            ),
            available_callback=(
                lambda: False
            ),
        )
    )

    manager.register(
        recognizer
    )

    with pytest.raises(
        RuntimeError
    ):
        manager.recognize(
            audio=stream.buffer,
            recognizer_name=(
                "offline-provider"
            ),
        )


def test_empty_audio_is_rejected():
    manager = VoiceRecognizerManager()

    stream = VoiceAudioStream(
        "stream-empty"
    )

    with pytest.raises(
        ValueError
    ):
        manager.recognize(
            stream.buffer
        )


def test_text_recognizer_remains_default():
    manager = VoiceRecognizerManager()

    manager.initialize()

    recognizers = (
        manager.recognizers()
    )

    text = next(
        item
        for item in recognizers
        if item["name"]
        == "text"
    )

    assert (
        text["available"]
        is True
    )

    assert (
        text["default"]
        is True
  )
