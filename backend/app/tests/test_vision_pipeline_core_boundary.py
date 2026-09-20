import time

from app.modules.vision.pipeline.pipeline_context import (
    PipelineContext,
)
from app.modules.vision.pipeline.pipeline_result import (
    PipelineResult,
)
from app.modules.vision.pipeline.pipeline_scheduler import (
    PipelineScheduler,
)


def test_pipeline_context_contract():
    context = PipelineContext(
        camera_id="camera-1",
        frame={
            "frame": 1,
        },
        metadata={
            "source": "test",
        },
    )

    context.update(
        analysis={
            "persons": 1,
        },
        events=[
            {
                "type": "motion",
            }
        ],
        decisions=[
            {
                "rule": "person_detected",
            }
        ],
        actions=[
            {
                "action": "notify",
            }
        ],
    )

    data = context.to_dict()

    assert (
        data["camera_id"]
        == "camera-1"
    )

    assert (
        data["analysis"][
            "persons"
        ]
        == 1
    )

    assert (
        len(
            data["events"]
        )
        == 1
    )

    assert (
        len(
            data["decisions"]
        )
        == 1
    )

    assert (
        len(
            data["actions"]
        )
        == 1
    )


def test_pipeline_result_success_contract():
    result = PipelineResult(
        camera_id="camera-1",
        analysis={
            "objects": 2,
        },
        events=[],
        decisions=[],
        actions=[],
    )

    data = result.to_dict()

    assert (
        data["success"]
        is True
    )

    assert (
        data["error"]
        is None
    )

    assert (
        data["analysis"][
            "objects"
        ]
        == 2
    )


def test_pipeline_result_failure_contract():
    result = PipelineResult(
        camera_id="camera-2",
        success=False,
        error="camera failure",
    )

    data = result.to_dict()

    assert (
        data["success"]
        is False
    )

    assert (
        data["error"]
        == "camera failure"
    )


def test_scheduler_runs_callback():
    scheduler = PipelineScheduler()

    counter = {
        "value": 0,
    }

    def callback():
        counter["value"] += 1

    assert (
        scheduler.start(
            callback,
            interval=0.01,
        )
        is True
    )

    time.sleep(
        0.06
    )

    scheduler.stop()

    assert (
        counter["value"]
        >= 1
    )

    assert (
        scheduler.cycles()
        >= 1
    )

    assert (
        scheduler.running()
        is False
    )


def test_scheduler_rejects_duplicate_start():
    scheduler = PipelineScheduler()

    def callback():
        return None

    assert (
        scheduler.start(
            callback,
            interval=0.02,
        )
        is True
    )

    assert (
        scheduler.start(
            callback,
            interval=0.02,
        )
        is False
    )

    scheduler.stop()


def test_scheduler_records_callback_error():
    scheduler = PipelineScheduler()

    def callback():
        raise RuntimeError(
            "vision processing error"
        )

    scheduler.start(
        callback,
        interval=0.01,
    )

    time.sleep(
        0.04
    )

    scheduler.stop()

    assert (
        scheduler.last_error()
        == "vision processing error"
    )

    status = scheduler.status()

    assert (
        status["running"]
        is False
    )

    assert (
        status["last_error"]
        == "vision processing error"
    )


def test_scheduler_clear_error():
    scheduler = PipelineScheduler()

    def callback():
        raise RuntimeError(
            "temporary error"
        )

    scheduler.start(
        callback,
        interval=0.01,
    )

    time.sleep(
        0.03
    )

    scheduler.stop()

    assert (
        scheduler.last_error()
        == "temporary error"
    )

    scheduler.clear_error()

    assert (
        scheduler.last_error()
        is None
    )


def test_scheduler_stop_is_idempotent():
    scheduler = PipelineScheduler()

    assert (
        scheduler.stop()
        is True
    )

    assert (
        scheduler.stop()
        is True
    )


def test_scheduler_status_contract():
    scheduler = PipelineScheduler()

    status = scheduler.status()

    assert {
        "running",
        "cycles",
        "last_error",
        "thread_alive",
    }.issubset(
        status.keys()
    )

    assert (
        status["running"]
        is False
    )

    assert (
        status["cycles"]
        == 0
  )
