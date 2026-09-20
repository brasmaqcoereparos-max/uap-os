from app.modules.vision.automation.vision_automation_bridge import (
    vision_automation_bridge,
)
from app.modules.vision.decision.decision_registry import (
    decision_registry,
)
from app.modules.vision.decision.decision_service import (
    decision_service,
)
from app.modules.vision.pipeline.pipeline_result import (
    PipelineResult,
)
from app.modules.vision.pipeline.pipeline_runner import (
    PipelineRunner,
)
from app.modules.vision.pipeline.vision_pipeline import (
    VisionPipeline,
)


def reset_rules():
    decision_registry.clear()


def test_pipeline_executes_safe_action(
    monkeypatch,
):
    reset_rules()

    pipeline = VisionPipeline()

    monkeypatch.setattr(
        pipeline,
        "analyze_frame",
        lambda camera_id, frame: {
            "motion": {
                "motion": True,
            },
            "persons": 0,
            "detections": [],
        },
    )

    decision_service.create(
        name="motion-action",
        conditions=[
            {
                "type": "motion",
                "value": True,
            }
        ],
        actions=[
            {
                "action": (
                    "automation.notify"
                ),
                "data": {
                    "message": (
                        "Movimento detectado"
                    ),
                },
            }
        ],
    )

    received = []

    vision_automation_bridge.register_action(
        "automation.notify",
        lambda data: (
            received.append(
                data
            )
            or {
                "accepted": True,
            }
        ),
    )

    result = pipeline.process(
        camera_id="camera-1",
        frame=object(),
    )

    assert (
        len(
            result["decisions"]
        )
        == 1
    )

    assert (
        len(
            result["actions"]
        )
        == 1
    )

    assert (
        len(
            result[
                "action_results"
            ]
        )
        == 1
    )

    assert (
        result[
            "action_results"
        ][0][
            "execution"
        ][
            "success"
        ]
        is True
    )

    assert (
        received[0][
            "message"
        ]
        == "Movimento detectado"
    )

    vision_automation_bridge.unregister_action(
        "automation.notify"
    )

    reset_rules()


def test_pipeline_keeps_action_request_and_result_separate(
    monkeypatch,
):
    reset_rules()

    pipeline = VisionPipeline()

    monkeypatch.setattr(
        pipeline,
        "analyze_frame",
        lambda camera_id, frame: {
            "persons": 1,
            "detections": [],
            "motion": {
                "motion": False,
            },
        },
    )

    decision_service.create(
        name="person-rule",
        conditions=[
            {
                "type": "person",
                "operator": ">=",
                "count": 1,
            }
        ],
        actions=[
            {
                "action": (
                    "automation.event"
                ),
                "data": {
                    "event": (
                        "person_detected"
                    ),
                },
            }
        ],
    )

    vision_automation_bridge.register_action(
        "automation.event",
        lambda data: {
            "event": data[
                "event"
            ],
        },
    )

    result = pipeline.process(
        "camera-2",
        object(),
    )

    assert (
        result["actions"][0][
            "rule"
        ]
        == "person-rule"
    )

    assert (
        result["actions"][0][
            "action"
        ][
            "action"
        ]
        == "automation.event"
    )

    assert (
        result[
            "action_results"
        ][0][
            "rule"
        ]
        == "person-rule"
    )

    vision_automation_bridge.unregister_action(
        "automation.event"
    )

    reset_rules()


def test_unknown_action_fails_without_breaking_pipeline(
    monkeypatch,
):
    reset_rules()

    pipeline = VisionPipeline()

    monkeypatch.setattr(
        pipeline,
        "analyze_frame",
        lambda camera_id, frame: {
            "persons": 1,
            "detections": [],
            "motion": {
                "motion": False,
            },
        },
    )

    decision_service.create(
        name="unknown-action",
        conditions=[
            {
                "type": "person",
                "operator": ">=",
                "count": 1,
            }
        ],
        actions=[
            {
                "action": (
                    "automation.not_registered"
                ),
            }
        ],
    )

    result = pipeline.process(
        "camera-3",
        object(),
    )

    execution = (
        result[
            "action_results"
        ][0][
            "execution"
        ]
    )

    assert (
        execution[
            "success"
        ]
        is False
    )

    assert (
        execution[
            "blocked"
        ]
        is False
    )

    reset_rules()


def test_pipeline_context_result_contract():
    result = PipelineResult(
        camera_id="camera-4",
        analysis={
            "persons": 1,
        },
        events=[
            {
                "event_type": (
                    "person_detected"
                ),
            }
        ],
        decisions=[
            {
                "name": (
                    "person-rule"
                ),
            }
        ],
        actions=[
            {
                "action": (
                    "automation.notify"
                ),
            }
        ],
        action_results=[
            {
                "execution": {
                    "success": True,
                },
            }
        ],
    )

    data = result.to_dict()

    assert (
        data["camera_id"]
        == "camera-4"
    )

    assert (
        len(
            data[
                "action_results"
            ]
        )
        == 1
    )

    assert (
        data[
            "action_results"
        ][0][
            "execution"
        ][
            "success"
        ]
        is True
    )


def test_pipeline_runner_preserves_action_results(
    monkeypatch,
):
    runner = PipelineRunner()

    from app.modules.vision.pipeline import (
        pipeline_runner,
    )

    monkeypatch.setattr(
        pipeline_runner.vision_pipeline,
        "process",
        lambda camera_id, frame: {
            "analysis": {
                "persons": 1,
            },
            "events": [],
            "decisions": [],
            "actions": [
                {
                    "action": (
                        "automation.notify"
                    ),
                }
            ],
            "action_results": [
                {
                    "execution": {
                        "success": True,
                    },
                }
            ],
        },
    )

    result = runner.run(
        camera_id="camera-5",
        frame=object(),
    )

    assert (
        result.success
        is True
    )

    assert (
        len(
            result.action_results
        )
        == 1
    )

    assert (
        result.action_results[
            0
        ][
            "execution"
        ][
            "success"
        ]
        is True
    )


def test_pipeline_runner_converts_error_to_result(
    monkeypatch,
):
    runner = PipelineRunner()

    from app.modules.vision.pipeline import (
        pipeline_runner,
    )

    def fail(
        camera_id,
        frame,
    ):
        raise RuntimeError(
            "vision failure"
        )

    monkeypatch.setattr(
        pipeline_runner.vision_pipeline,
        "process",
        fail,
    )

    result = runner.run(
        camera_id="camera-error",
        frame=object(),
    )

    assert (
        result.success
        is False
    )

    assert (
        result.error
        == "vision failure"
    )

    assert (
        result.action_results
        == []
  )
